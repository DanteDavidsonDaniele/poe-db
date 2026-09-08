from __future__ import annotations
from dataclasses import dataclass
from pydantic import BaseModel, ConfigDict, ValidationError


class LeaguesParseError(Exception):
    pass


class _WireLeague(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    realm: str | None = None
    text: str | None = None


class _WireLeaguesResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    result: list[_WireLeague] | None = None


@dataclass(frozen=True)
class League:
    id: str
    realm: str
    text: str


def parse_leagues(payload: object) -> list[League]:
    try:
        wire = _WireLeaguesResponse.model_validate(payload)
    except ValidationError as exc:
        raise LeaguesParseError("payload is not a leagues response") from exc

    if wire.result is None:
        raise LeaguesParseError("response has no 'result' key")

    return [
        League(id=item.id, realm=item.realm, text=item.text)
        for item in wire.result
        if item.id and item.realm and item.text
    ]