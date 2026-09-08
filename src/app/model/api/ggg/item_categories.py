from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict, ValidationError


class ItemCategoriesParseError(Exception):
    pass


class _WireEntry(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: str | None = None
    text: str | None = None
    name: str | None = None
    flags: dict[str, object] | None = None


class _WireItemCategory(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str | None = None
    label: str | None = None
    entries: list[_WireEntry] | None = None


class _WireItemsResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    result: list[_WireItemCategory] | None = None


@dataclass(frozen=True)
class ItemCategoryEntry:
    type: str
    text: str
    name: str | None
    flags: frozenset[str]

    @property
    def is_unique(self) -> bool:
        return "unique" in self.flags


@dataclass(frozen=True)
class ItemCategory:
    id: str
    label: str
    entries: tuple[ItemCategoryEntry, ...]


def _to_flags(raw: dict[str, object] | None) -> frozenset[str]:
    return frozenset(key for key, value in (raw or {}).items() if value is True)


def _to_entry(entry: _WireEntry) -> ItemCategoryEntry | None:
    if not entry.type or not entry.text:
        return None
    return ItemCategoryEntry(
        type=entry.type,
        text=entry.text,
        name=entry.name or None,
        flags=_to_flags(entry.flags),
    )


def parse_item_categories(payload: object) -> list[ItemCategory]:
    try:
        wire = _WireItemsResponse.model_validate(payload)
    except ValidationError as exc:
        raise ItemCategoriesParseError("payload is not an items response") from exc

    if wire.result is None:
        raise ItemCategoriesParseError("response has no 'result' key")

    return [
        ItemCategory(
            id=category.id,
            label=category.label,
            entries=tuple(
                filter(None, (_to_entry(e) for e in category.entries or []))
            ),
        )
        for category in wire.result
        if category.id and category.label
    ]