"""Minimal Buffer GraphQL client using only the Python stdlib."""

import json
import os
import urllib.error
import urllib.request


API_URL = "https://api.buffer.com/graphql"
USER_AGENT = "buffer-social-scheduler/1.0"


class BufferError(Exception):
    """Raised when the Buffer API returns an error."""


class BufferClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("BUFFER_API_KEY")
        if not self.api_key:
            raise BufferError(
                "BUFFER_API_KEY not set. Export it in your shell or pass api_key=..."
            )

    def _request(self, query, variables=None):
        payload = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
        req = urllib.request.Request(
            API_URL,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
                "User-Agent": USER_AGENT,
            },
        )
        try:
            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            raise BufferError(f"HTTP {e.code}: {body}") from e
        if "errors" in result:
            raise BufferError(f"GraphQL errors: {result['errors']}")
        return result["data"]

    def list_channels(self):
        """Return a flat list of channels across all organizations."""
        query = """
        {
          account {
            organizations {
              id
              name
              channels {
                id
                name
                service
              }
            }
          }
        }
        """
        data = self._request(query)
        channels = []
        for org in data["account"]["organizations"]:
            for ch in org["channels"]:
                channels.append(
                    {
                        "id": ch["id"],
                        "name": ch["name"],
                        "service": ch["service"],
                        "organization_id": org["id"],
                        "organization_name": org["name"],
                    }
                )
        return channels

    def create_post(self, text, channel_id, due_at, image_url=None, video_url=None):
        """Schedule a single post. Returns the buffer post id and due_at.

        Raises BufferError on rejection (duplicate, validation, etc.).
        """
        input_data = {
            "text": text,
            "channelId": channel_id,
            "schedulingType": "automatic",
            "mode": "customScheduled",
            "dueAt": due_at,
        }
        assets = {}
        if image_url:
            assets["images"] = [{"url": image_url}]
        if video_url:
            assets["videos"] = [{"url": video_url}]
        if assets:
            input_data["assets"] = assets

        query = """
        mutation CreatePost($input: CreatePostInput!) {
          createPost(input: $input) {
            ... on PostActionSuccess { post { id dueAt } }
            ... on MutationError { message }
          }
        }
        """
        data = self._request(query, {"input": input_data})
        payload = data.get("createPost", {})
        if "post" in payload:
            return {"id": payload["post"]["id"], "due_at": payload["post"]["dueAt"]}
        if "message" in payload:
            raise BufferError(payload["message"])
        raise BufferError(f"Unexpected createPost response: {payload}")

    def delete_post(self, post_id):
        """Delete a scheduled post. Returns True on success."""
        query = (
            "mutation { deletePost(input: { id: \"%s\" }) { __typename } }" % post_id
        )
        data = self._request(query)
        typename = data.get("deletePost", {}).get("__typename")
        return typename == "DeletePostSuccess"
