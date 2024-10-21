import datetime  # noqa: D104

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):  # noqa: D101
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)

    # Basic Auth Info
    username: Mapped[str] = mapped_column(String(16))
    hashed_password = mapped_column(String(128))  # Use Argon2id

    # Adv Auth Info
    email: Mapped[str] = mapped_column(String(32))
    mtf_verified: Mapped[bool] = mapped_column(default=False)

    # Account Status
    activated: Mapped[bool] = mapped_column(default=False)
    read_only: Mapped[bool] = mapped_column(default=False)
    can_login: Mapped[bool] = mapped_column(default=True)
    shadow_banned: Mapped[bool] = mapped_column(default=False)  # Reserved Column

    # Personal Info
    nickname: Mapped[str] = mapped_column(String(32))
    avatar_url: Mapped[str | None] = mapped_column(String(96))
    bio: Mapped[str | None] = mapped_column(Text())
    birth: Mapped[datetime.date | None]
    joined_at: Mapped[datetime.datetime]
    website: Mapped[str | None] = mapped_column(String(64))
    phone: Mapped[str | None] = mapped_column(String(16))

    def __repr__(self) -> str:  # noqa: D105
        return (
            f"<User(id={self.id}, username={self.username}, "
            f"activated={self.activated})>"
        )


class OAuthApp(Base):  # noqa: D101
    __tablename__ = "oauth_apps"
    id: Mapped[int] = mapped_column(primary_key=True)
    app_name: Mapped[str] = mapped_column(String(30))
    app_desc: Mapped[str] = mapped_column(String(256))
    client_id: Mapped[str] = mapped_column(String(32), unique=True)
    client_secret: Mapped[str] = mapped_column(String(32))
    redirect_uri: Mapped[str] = mapped_column(String(256))
    allowed_scopes: Mapped[str] = mapped_column(String(256))

    def __repr__(self) -> str:  # noqa: D105
        return f"<OAuthApp(client_id={self.client_id})>"


class Code(Base):  # noqa: D101
    __tablename__ = "codes"
    code: Mapped[str] = mapped_column(String(32), primary_key=True)
    client_id: Mapped[str] = mapped_column(String(32))
    scope: Mapped[str] = mapped_column(String(256))
    redirect_uri: Mapped[str] = mapped_column(String(256))
    access_token: Mapped[str] = mapped_column(String(32))
    id_token: Mapped[str] = mapped_column(String(1024))

    def __repr__(self) -> str:  # noqa: D105
        return f"<Code(code={self.code})>"
