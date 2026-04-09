from typing import Annotated

from pydantic import AfterValidator, BaseModel, Field

from app.validators import no_forbidden_words


class User(BaseModel):
    username: str
    user_info: str


class Feedback(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=50)]
    message: Annotated[str, Field(min_length=10, max_length=500), AfterValidator(no_forbidden_words)]
