from __future__ import annotations
from dataclasses import dataclass
from pydantic import BaseModel, ConfigDict, ValidationError


class StatsParseError(Exception):
    pass


class _WireStatCategoryEntry(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    type: str | None = None
    text: str | None = None

class _WireStatCategory(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    label: str | None = None
    entries: list[_WireStatCategoryEntry] | None = None


class _WireStatResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    result: list[_WireStatCategory] | None = None

@dataclass(frozen=True)
class Stat:
    id: str
    type: str
    text: str

def parse_stats(payload: object) -> list[Stat]:
    try:
        wire = _WireStatResponse.model_validate(payload)
    except ValidationError as exc:
        raise StatsParseError("payload is not a stats response") from exc

    if wire.result is None:
        raise StatsParseError("response has no 'result' key")

    return [
        Stat(id=entry.id, type=entry.type, text=entry.text)
        for category in wire.result
        for entry in category.entries or []
        if entry.id and entry.type and entry.text
    ]