from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict, ValidationError


class TradeParseError(Exception):
    pass



class _WireTradeResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    complexity: int | None = None
    id: str | None
    inexact: bool | None = None
    result: list[str] | None = None
    total: int | None = None


@dataclass(frozen=True)
class TradeResponse:
    complexity: int
    id: str 
    inexact: bool
    result: list[str]
    total: int



def parse_trade_response(payload: object) -> TradeResponse:
    try:
        wire = _WireTradeResponse.model_validate(payload)
    except ValidationError as exc:
        raise TradeParseError("payload is not an trade response") from exc

    return TradeResponse(
            id=wire.id,
            complexity=wire.complexity,
            result= wire.result,
            inexact= wire.inexact,
            total=wire.total
        )

