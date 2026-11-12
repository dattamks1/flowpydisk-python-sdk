"""Generated from the FlowpyDisk OpenAPI spec. DO NOT EDIT.

677 operations across 34 namespaces.

The generator lives in the FlowpyDisk source repo, and a test there fails
if this file and the spec disagree. Changes here are made by regenerating,
never by hand.
"""

from __future__ import annotations

from typing import Any


class _Namespace:
    """Holds the client every generated method calls through."""

    def __init__(self, client: Any) -> None:
        self._c = client


class AccountOps(_Namespace):
    """13 operations."""

    def delete_avatar(self, **params: Any) -> Any:
        """Clear the profile picture

        ``DELETE /auth/account/avatar``
        """
        return self._c.request("DELETE", "auth/account/avatar", params=params)

    def update_avatar(self, *, json: Any = None, **params: Any) -> Any:
        """Set the profile picture (owner session only)

        ``PATCH /auth/account/avatar``
        """
        return self._c.request("PATCH", "auth/account/avatar", json=json, params=params)

    def create_consent(self, *, json: Any = None, **params: Any) -> Any:
        """Record ToS/policy acceptance

        ``POST /auth/account/consent``
        """
        return self._c.request("POST", "auth/account/consent", json=json, params=params)

    def create_restore(self, *, json: Any = None, **params: Any) -> Any:
        """Restore a deleted account inside its 30 days

        ``POST /auth/account/restore``
        """
        return self._c.request("POST", "auth/account/restore", json=json, params=params)

    def list_settings(self, **params: Any) -> Any:
        """Get account preferences

        ``GET /auth/account/settings``
        """
        return self._c.request("GET", "auth/account/settings", params=params)

    def update_settings(self, *, json: Any = None, **params: Any) -> Any:
        """Update account preferences

        ``PATCH /auth/account/settings``
        """
        return self._c.request("PATCH", "auth/account/settings", json=json, params=params)

    def list_username(self, **params: Any) -> Any:
        """Your username and when you may change it

        ``GET /auth/account/username``
        """
        return self._c.request("GET", "auth/account/username", params=params)

    def update_username(self, *, json: Any = None, **params: Any) -> Any:
        """Choose your username

        ``PUT /auth/account/username``
        """
        return self._c.request("PUT", "auth/account/username", json=json, params=params)

    def list_check(self, **params: Any) -> Any:
        """Whether you may take a username

        ``GET /auth/account/username/check``
        """
        return self._c.request("GET", "auth/account/username/check", params=params)

    def list_api_keys(self, **params: Any) -> Any:
        """List API keys (secrets never returned)

        ``GET /auth/api-keys``
        """
        return self._c.request("GET", "auth/api-keys", params=params)

    def list_mcp_connect(self, **params: Any) -> Any:
        """The hosted MCP server's address, for connecting an assistant

        ``GET /auth/mcp-connect``
        """
        return self._c.request("GET", "auth/mcp-connect", params=params)

    def get_people(self, username: str, **params: Any) -> Any:
        """Find a person by their username

        ``GET /auth/people/{username}``
        """
        return self._c.request("GET", f"auth/people/{username}", params=params)

    def create_live_pass(self, *, json: Any = None, **params: Any) -> Any:
        """A pass for your imail realtime channel

        ``POST /mail/live-pass``
        """
        return self._c.request("POST", "mail/live-pass", json=json, params=params)


class AuthOps(_Namespace):
    """48 operations."""

    def list_challenge(self, **params: Any) -> Any:
        """How to sign in to THIS deployment

        ``GET /auth/challenge``
        """
        return self._c.request("GET", "auth/challenge", params=params)

    def list_csrf(self, **params: Any) -> Any:
        """Prime the CSRF cookie

        ``GET /auth/csrf``
        """
        return self._c.request("GET", "auth/csrf", params=params)

    def list_devices(self, **params: Any) -> Any:
        """Devices signed in to this account

        ``GET /auth/devices``
        """
        return self._c.request("GET", "auth/devices", params=params)

    def create_devices(self, *, json: Any = None, **params: Any) -> Any:
        """Register this device

        ``POST /auth/devices``
        """
        return self._c.request("POST", "auth/devices", json=json, params=params)

    def create_join(self, *, json: Any = None, **params: Any) -> Any:
        """Join FlowpyDisk with an existing INVRSYS login (D5)

        ``POST /auth/join``
        """
        return self._c.request("POST", "auth/join", json=json, params=params)

    def create_login(self, *, json: Any = None, **params: Any) -> Any:
        """Log in

        ``POST /auth/login``
        """
        return self._c.request("POST", "auth/login", json=json, params=params)

    def list_login_history(self, **params: Any) -> Any:
        """Recent successful sign-ins (Settings → Security)

        ``GET /auth/login-history``
        """
        return self._c.request("GET", "auth/login-history", params=params)

    def create_logout(self, *, json: Any = None, **params: Any) -> Any:
        """Log out

        ``POST /auth/logout``
        """
        return self._c.request("POST", "auth/logout", json=json, params=params)

    def list_me(self, **params: Any) -> Any:
        """Current user

        ``GET /auth/me``
        """
        return self._c.request("GET", "auth/me", params=params)

    def create_password_change(self, *, json: Any = None, **params: Any) -> Any:
        """Change your password while signed in

        ``POST /auth/password-change``
        """
        return self._c.request("POST", "auth/password-change", json=json, params=params)

    def create_password_reset(self, *, json: Any = None, **params: Any) -> Any:
        """Request a password reset (never reveals account existence)

        ``POST /auth/password-reset``
        """
        return self._c.request("POST", "auth/password-reset", json=json, params=params)

    def create_check(self, *, json: Any = None, **params: Any) -> Any:
        """Is this reset link still good

        ``POST /auth/password-reset/check``
        """
        return self._c.request("POST", "auth/password-reset/check", json=json, params=params)

    def create_confirm(self, *, json: Any = None, **params: Any) -> Any:
        """Confirm a password reset

        ``POST /auth/password-reset/confirm``
        """
        return self._c.request("POST", "auth/password-reset/confirm", json=json, params=params)

    def list_phone(self, **params: Any) -> Any:
        """The account's mobile number, and whether it must be added (4z30)

        ``GET /auth/phone/``
        """
        return self._c.request("GET", "auth/phone/", params=params)

    def create_change(self, *, json: Any = None, **params: Any) -> Any:
        """Confirm it is you before Change number (4z31)

        ``POST /auth/phone/change``
        """
        return self._c.request("POST", "auth/phone/change", json=json, params=params)

    def create_code(self, *, json: Any = None, **params: Any) -> Any:
        """Send a code on WhatsApp to a mobile number (4z30)

        ``POST /auth/phone/code``
        """
        return self._c.request("POST", "auth/phone/code", json=json, params=params)

    def create_sign_in_code(self, *, json: Any = None, **params: Any) -> Any:
        """Passwordless sign-in, step 1 - a code on WhatsApp (4z30)

        ``POST /auth/phone/sign-in/code``
        """
        return self._c.request("POST", "auth/phone/sign-in/code", json=json, params=params)

    def create_verify(self, *, json: Any = None, **params: Any) -> Any:
        """Passwordless sign-in, step 2 - the code, for Cognito's custom challenge (4z30)

        ``POST /auth/phone/sign-in/verify``
        """
        return self._c.request("POST", "auth/phone/sign-in/verify", json=json, params=params)

    def create_snooze(self, *, json: Any = None, **params: Any) -> Any:
        """Not now on the mobile number prompt, remembered on the account for 7 days (M2722.2)

        ``POST /auth/phone/snooze``
        """
        return self._c.request("POST", "auth/phone/snooze", json=json, params=params)

    def create_phone_verify(self, *, json: Any = None, **params: Any) -> Any:
        """Check a WhatsApp code (4z30)

        ``POST /auth/phone/verify``
        """
        return self._c.request("POST", "auth/phone/verify", json=json, params=params)

    def create_provision(self, *, json: Any = None, **params: Any) -> Any:
        """Turn a verified identity token into an account here

        ``POST /auth/provision``
        """
        return self._c.request("POST", "auth/provision", json=json, params=params)

    def create_register(self, *, json: Any = None, **params: Any) -> Any:
        """Register (email/password)

        ``POST /auth/register``
        """
        return self._c.request("POST", "auth/register", json=json, params=params)

    def create_session(self, *, json: Any = None, **params: Any) -> Any:
        """Trade a verified token for a browser session cookie

        ``POST /auth/session``
        """
        return self._c.request("POST", "auth/session", json=json, params=params)

    def create_session_exchange(self, *, json: Any = None, **params: Any) -> Any:
        """Hand a signed-in browser session to a native client

        ``POST /auth/session-exchange``
        """
        return self._c.request("POST", "auth/session-exchange", json=json, params=params)

    def create_signup_confirm(self, *, json: Any = None, **params: Any) -> Any:
        """Confirm a sign-up code by address, from the sign-in screen

        ``POST /auth/signup/confirm``
        """
        return self._c.request("POST", "auth/signup/confirm", json=json, params=params)

    def create_new_code(self, *, json: Any = None, **params: Any) -> Any:
        """Send a new sign-up code by address, from the sign-in screen

        ``POST /auth/signup/new-code``
        """
        return self._c.request("POST", "auth/signup/new-code", json=json, params=params)

    def list_check(self, **params: Any) -> Any:
        """Check a User ID at sign-up, before the account exists (BA11)

        ``GET /auth/username/check``
        """
        return self._c.request("GET", "auth/username/check", params=params)

    def create_verify_email(self, *, json: Any = None, **params: Any) -> Any:
        """Verify email with the emailed code

        ``POST /auth/verify-email``
        """
        return self._c.request("POST", "auth/verify-email", json=json, params=params)

    def create_resend(self, *, json: Any = None, **params: Any) -> Any:
        """Send the verification code again

        ``POST /auth/verify-email/resend``
        """
        return self._c.request("POST", "auth/verify-email/resend", json=json, params=params)

    def list_approvals(self, **params: Any) -> Any:
        """The approvals connected apps asked this person for (PIPELINE §5.20)

        ``GET /connectors/approvals``
        """
        return self._c.request("GET", "connectors/approvals", params=params)

    def create_approvals(self, *, json: Any = None, **params: Any) -> Any:
        """A connected app asks its person to approve one destructive call

        ``POST /connectors/approvals``
        """
        return self._c.request("POST", "connectors/approvals", json=json, params=params)

    def create_approvals_consume(self, *, json: Any = None, **params: Any) -> Any:
        """Consume an approval without performing an operation (legacy)

        ``POST /connectors/approvals/consume``
        """
        return self._c.request("POST", "connectors/approvals/consume", json=json, params=params)

    def get_email(self, token: str, **params: Any) -> Any:
        """Read the request behind an email's one-click link

        ``GET /connectors/approvals/email/{token}``
        """
        return self._c.request("GET", f"connectors/approvals/email/{token}", params=params)

    def create_email(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Answer from the email

        ``POST /connectors/approvals/email/{token}``
        """
        return self._c.request("POST", f"connectors/approvals/email/{token}", json=json, params=params)

    def get_approvals(self, approval_id: str, **params: Any) -> Any:
        """One approval request

        ``GET /connectors/approvals/{approval_id}``
        """
        return self._c.request("GET", f"connectors/approvals/{approval_id}", params=params)

    def approve_approvals(self, approval_id: str, *, json: Any = None, **params: Any) -> Any:
        """The person approves

        ``POST /connectors/approvals/{approval_id}/approve``
        """
        return self._c.request("POST", f"connectors/approvals/{approval_id}/approve", json=json, params=params)

    def deny_approvals(self, approval_id: str, *, json: Any = None, **params: Any) -> Any:
        """The person denies

        ``POST /connectors/approvals/{approval_id}/deny``
        """
        return self._c.request("POST", f"connectors/approvals/{approval_id}/deny", json=json, params=params)

    def list_sessions(self, **params: Any) -> Any:
        """Apps connected to this account

        ``GET /connectors/sessions``
        """
        return self._c.request("GET", "connectors/sessions", params=params)

    def get_sessions(self, session_id: str, **params: Any) -> Any:
        """One connection, with what could be granted and its history

        ``GET /connectors/sessions/{session_id}``
        """
        return self._c.request("GET", f"connectors/sessions/{session_id}", params=params)

    def update_sessions(self, session_id: str, *, json: Any = None, **params: Any) -> Any:
        """Edit what an app may reach (owner, 2026-09-07)

        ``PATCH /connectors/sessions/{session_id}``
        """
        return self._c.request("PATCH", f"connectors/sessions/{session_id}", json=json, params=params)

    def list_openid_configuration(self, **params: Any) -> Any:
        """OIDC discovery document

        ``GET /oauth/.well-known/openid-configuration``
        """
        return self._c.request("GET", "oauth/.well-known/openid-configuration", params=params)

    def list_authorize(self, **params: Any) -> Any:
        """Authorisation endpoint

        ``GET /oauth/authorize``
        """
        return self._c.request("GET", "oauth/authorize", params=params)

    def get_icon_clients(self, client_id: str, **params: Any) -> Any:
        """A registered app's icon, from our origin

        ``GET /oauth/clients/{client_id}/icon``
        """
        return self._c.request("GET", f"oauth/clients/{client_id}/icon", params=params)

    def create_consent(self, *, json: Any = None, **params: Any) -> Any:
        """Approve a third-party app

        ``POST /oauth/consent``
        """
        return self._c.request("POST", "oauth/consent", json=json, params=params)

    def list_jwks_json(self, **params: Any) -> Any:
        """The public keys tokens are signed with

        ``GET /oauth/jwks.json``
        """
        return self._c.request("GET", "oauth/jwks.json", params=params)

    def create_oauth_register(self, *, json: Any = None, **params: Any) -> Any:
        """Register an app (RFC 7591)

        ``POST /oauth/register``
        """
        return self._c.request("POST", "oauth/register", json=json, params=params)

    def create_revoke(self, *, json: Any = None, **params: Any) -> Any:
        """Revoke a token

        ``POST /oauth/revoke``
        """
        return self._c.request("POST", "oauth/revoke", json=json, params=params)

    def create_token(self, *, json: Any = None, **params: Any) -> Any:
        """Exchange a code, or refresh

        ``POST /oauth/token``
        """
        return self._c.request("POST", "oauth/token", json=json, params=params)


class BackupsOps(_Namespace):
    """7 operations."""

    def list_backups(self, **params: Any) -> Any:
        """Snapshot days

        ``GET /backups/``
        """
        return self._c.request("GET", "backups/", params=params)

    def get_restores(self, job_id: str, **params: Any) -> Any:
        """A restore's progress

        ``GET /backups/restores/{job_id}``
        """
        return self._c.request("GET", f"backups/restores/{job_id}", params=params)

    def get_items_restores(self, job_id: str, **params: Any) -> Any:
        """What a restore did with each item

        ``GET /backups/restores/{job_id}/items``
        """
        return self._c.request("GET", f"backups/restores/{job_id}/items", params=params)

    def restore_backups(self, day: str, *, json: Any = None, **params: Any) -> Any:
        """Restore chosen items

        ``POST /backups/{day}/restore``
        """
        return self._c.request("POST", f"backups/{day}/restore", json=json, params=params)

    def restore_all_backups(self, day: str, *, json: Any = None, **params: Any) -> Any:
        """Restore everything from a day

        ``POST /backups/{day}/restore-all``
        """
        return self._c.request("POST", f"backups/{day}/restore-all", json=json, params=params)

    def get_sections_backups(self, day: str, **params: Any) -> Any:
        """What one day holds, per section

        ``GET /backups/{day}/sections``
        """
        return self._c.request("GET", f"backups/{day}/sections", params=params)

    def get_backups(self, day: str, section: str, **params: Any) -> Any:
        """Browse one section of a day

        ``GET /backups/{day}/{section}``
        """
        return self._c.request("GET", f"backups/{day}/{section}", params=params)


class BannersOps(_Namespace):
    """3 operations."""

    def list_banners(self, **params: Any) -> Any:
        """The banners for this person in one slot

        ``GET /banners``
        """
        return self._c.request("GET", "banners", params=params)

    def dismiss_banners(self, banner_id: str, *, json: Any = None, **params: Any) -> Any:
        """Dismiss a banner for this person, on every device

        ``POST /banners/{banner_id}/dismiss``
        """
        return self._c.request("POST", f"banners/{banner_id}/dismiss", json=json, params=params)

    def events_banners(self, banner_id: str, *, json: Any = None, **params: Any) -> Any:
        """Count a view or a tap

        ``POST /banners/{banner_id}/events``
        """
        return self._c.request("POST", f"banners/{banner_id}/events", json=json, params=params)


class BillingOps(_Namespace):
    """12 operations."""

    def get_pdf_credit_notes(self, credit_note_id: str, **params: Any) -> Any:
        """One of the account's credit notes as a PDF

        ``GET /billing/credit-notes/{credit_note_id}/pdf``
        """
        return self._c.request("GET", f"billing/credit-notes/{credit_note_id}/pdf", params=params)

    def list_invoices(self, **params: Any) -> Any:
        """The account's invoices and credit notes

        ``GET /billing/invoices``
        """
        return self._c.request("GET", "billing/invoices", params=params)

    def get_pdf_invoices(self, invoice_id: str, **params: Any) -> Any:
        """One of the account's invoices as a PDF

        ``GET /billing/invoices/{invoice_id}/pdf``
        """
        return self._c.request("GET", f"billing/invoices/{invoice_id}/pdf", params=params)

    def list_limits(self, **params: Any) -> Any:
        """What the plan allows and how much of it is used

        ``GET /billing/limits``
        """
        return self._c.request("GET", "billing/limits", params=params)

    def list_mailbox_addon(self, **params: Any) -> Any:
        """The account's extra mailboxes, the offer, the counts and the next bill

        ``GET /billing/mailbox-addon``
        """
        return self._c.request("GET", "billing/mailbox-addon", params=params)

    def list_profile(self, **params: Any) -> Any:
        """The customer's billing details

        ``GET /billing/profile``
        """
        return self._c.request("GET", "billing/profile", params=params)

    def list_subscription(self, **params: Any) -> Any:
        """The account's plan, allowance, capability entitlements and catalogue

        ``GET /billing/subscription``
        """
        return self._c.request("GET", "billing/subscription", params=params)

    def create_razorpay(self, *, json: Any = None, **params: Any) -> Any:
        """Razorpay server-to-server webhook (not a client endpoint)

        ``POST /billing/webhook/razorpay``
        """
        return self._c.request("POST", "billing/webhook/razorpay", json=json, params=params)

    def create_preview(self, *, json: Any = None, **params: Any) -> Any:
        """Try a coupon code without using it

        ``POST /coupons/preview``
        """
        return self._c.request("POST", "coupons/preview", json=json, params=params)

    def create_redeem(self, *, json: Any = None, **params: Any) -> Any:
        """Redeem a free-months or AI-credits coupon

        ``POST /coupons/redeem``
        """
        return self._c.request("POST", "coupons/redeem", json=json, params=params)

    def list_redemptions(self, **params: Any) -> Any:
        """The coupons this account has used

        ``GET /coupons/redemptions``
        """
        return self._c.request("GET", "coupons/redemptions", params=params)

    def list_check(self, **params: Any) -> Any:
        """Check an invite code before sign-up (BA8)

        ``GET /referrals/check``
        """
        return self._c.request("GET", "referrals/check", params=params)


class BookingOps(_Namespace):
    """16 operations."""

    def list_booking_pages(self, **params: Any) -> Any:
        """List your booking pages

        ``GET /booking-pages``
        """
        return self._c.request("GET", "booking-pages", params=params)

    def create_booking_pages(self, *, json: Any = None, **params: Any) -> Any:
        """Create a booking page

        ``POST /booking-pages``
        """
        return self._c.request("POST", "booking-pages", json=json, params=params)

    def delete_booking_pages(self, page_id: str, **params: Any) -> Any:
        """Move a booking page to trash

        ``DELETE /booking-pages/{page_id}``
        """
        return self._c.request("DELETE", f"booking-pages/{page_id}", params=params)

    def get_booking_pages(self, page_id: str, **params: Any) -> Any:
        """Read one booking page

        ``GET /booking-pages/{page_id}``
        """
        return self._c.request("GET", f"booking-pages/{page_id}", params=params)

    def update_booking_pages(self, page_id: str, *, json: Any = None, **params: Any) -> Any:
        """Update a booking page

        ``PATCH /booking-pages/{page_id}``
        """
        return self._c.request("PATCH", f"booking-pages/{page_id}", json=json, params=params)

    def get_bookings_booking_pages(self, page_id: str, **params: Any) -> Any:
        """Who has booked time on this page

        ``GET /booking-pages/{page_id}/bookings``
        """
        return self._c.request("GET", f"booking-pages/{page_id}/bookings", params=params)

    def approve_bookings(self, page_id: str, booking_id: str, *, json: Any = None, **params: Any) -> Any:
        """Accept a pending request

        ``POST /booking-pages/{page_id}/bookings/{booking_id}/approve``
        """
        return self._c.request(
            "POST", f"booking-pages/{page_id}/bookings/{booking_id}/approve", json=json, params=params
        )

    def cancel_bookings(self, page_id: str, booking_id: str, *, json: Any = None, **params: Any) -> Any:
        """Cancel a confirmed booking

        ``POST /booking-pages/{page_id}/bookings/{booking_id}/cancel``
        """
        return self._c.request(
            "POST", f"booking-pages/{page_id}/bookings/{booking_id}/cancel", json=json, params=params
        )

    def decline_bookings(self, page_id: str, booking_id: str, *, json: Any = None, **params: Any) -> Any:
        """Decline a pending request

        ``POST /booking-pages/{page_id}/bookings/{booking_id}/decline``
        """
        return self._c.request(
            "POST", f"booking-pages/{page_id}/bookings/{booking_id}/decline", json=json, params=params
        )

    def move_bookings(self, page_id: str, booking_id: str, *, json: Any = None, **params: Any) -> Any:
        """Move a confirmed booking

        ``POST /booking-pages/{page_id}/bookings/{booking_id}/move``
        """
        return self._c.request("POST", f"booking-pages/{page_id}/bookings/{booking_id}/move", json=json, params=params)

    def purge_booking_pages(self, page_id: str, *, json: Any = None, **params: Any) -> Any:
        """Delete a trashed booking page permanently

        ``POST /booking-pages/{page_id}/purge``
        """
        return self._c.request("POST", f"booking-pages/{page_id}/purge", json=json, params=params)

    def get_slots_booking_pages(self, page_id: str, **params: Any) -> Any:
        """The bookable slots, with busy time already removed

        ``GET /booking-pages/{page_id}/slots``
        """
        return self._c.request("GET", f"booking-pages/{page_id}/slots", params=params)

    def get_windows_booking_pages(self, page_id: str, **params: Any) -> Any:
        """The weekly availability windows

        ``GET /booking-pages/{page_id}/windows``
        """
        return self._c.request("GET", f"booking-pages/{page_id}/windows", params=params)

    def windows_booking_pages(self, page_id: str, *, json: Any = None, **params: Any) -> Any:
        """Add a weekly window

        ``POST /booking-pages/{page_id}/windows``
        """
        return self._c.request("POST", f"booking-pages/{page_id}/windows", json=json, params=params)

    def delete_windows(self, page_id: str, window_id: str, **params: Any) -> Any:
        """Remove a window

        ``DELETE /booking-pages/{page_id}/windows/{window_id}``
        """
        return self._c.request("DELETE", f"booking-pages/{page_id}/windows/{window_id}", params=params)

    def update_windows(self, page_id: str, window_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change a window

        ``PATCH /booking-pages/{page_id}/windows/{window_id}``
        """
        return self._c.request("PATCH", f"booking-pages/{page_id}/windows/{window_id}", json=json, params=params)


class CalendarOps(_Namespace):
    """16 operations."""

    def list_calendar(self, **params: Any) -> Any:
        """The calendar view - events plus anything else dated

        ``GET /calendar``
        """
        return self._c.request("GET", "calendar", params=params)

    def list_events(self, **params: Any) -> Any:
        """List events

        ``GET /calendar/events``
        """
        return self._c.request("GET", "calendar/events", params=params)

    def create_events(self, *, json: Any = None, **params: Any) -> Any:
        """Create an event

        ``POST /calendar/events``
        """
        return self._c.request("POST", "calendar/events", json=json, params=params)

    def delete_events(self, event_id: str, **params: Any) -> Any:
        """Move an event to trash

        ``DELETE /calendar/events/{event_id}``
        """
        return self._c.request("DELETE", f"calendar/events/{event_id}", params=params)

    def get_events(self, event_id: str, **params: Any) -> Any:
        """Read one event

        ``GET /calendar/events/{event_id}``
        """
        return self._c.request("GET", f"calendar/events/{event_id}", params=params)

    def update_events(self, event_id: str, *, json: Any = None, **params: Any) -> Any:
        """Update an event

        ``PATCH /calendar/events/{event_id}``
        """
        return self._c.request("PATCH", f"calendar/events/{event_id}", json=json, params=params)

    def forward_events(self, event_id: str, *, json: Any = None, **params: Any) -> Any:
        """Forward an event you are invited to

        ``POST /calendar/events/{event_id}/forward``
        """
        return self._c.request("POST", f"calendar/events/{event_id}/forward", json=json, params=params)

    def purge_events(self, event_id: str, *, json: Any = None, **params: Any) -> Any:
        """Delete a trashed event permanently

        ``POST /calendar/events/{event_id}/purge``
        """
        return self._c.request("POST", f"calendar/events/{event_id}/purge", json=json, params=params)

    def reply_events(self, event_id: str, *, json: Any = None, **params: Any) -> Any:
        """Reply to an event you are invited to

        ``POST /calendar/events/{event_id}/reply``
        """
        return self._c.request("POST", f"calendar/events/{event_id}/reply", json=json, params=params)

    def list_calendars(self, **params: Any) -> Any:
        """List calendars on one connected Google or Outlook account

        ``GET /calendar/sync/calendars``
        """
        return self._c.request("GET", "calendar/sync/calendars", params=params)

    def list_conflicts(self, **params: Any) -> Any:
        """List unresolved calendar sync conflicts

        ``GET /calendar/sync/conflicts``
        """
        return self._c.request("GET", "calendar/sync/conflicts", params=params)

    def resolve_conflicts(self, conflict_id: str, *, json: Any = None, **params: Any) -> Any:
        """Resolve one calendar sync conflict

        ``POST /calendar/sync/conflicts/{conflict_id}/resolve``
        """
        return self._c.request("POST", f"calendar/sync/conflicts/{conflict_id}/resolve", json=json, params=params)

    def list_subscriptions(self, **params: Any) -> Any:
        """List the owner's calendar sync subscriptions

        ``GET /calendar/sync/subscriptions``
        """
        return self._c.request("GET", "calendar/sync/subscriptions", params=params)

    def create_subscriptions(self, *, json: Any = None, **params: Any) -> Any:
        """Opt one connected calendar into sync

        ``POST /calendar/sync/subscriptions``
        """
        return self._c.request("POST", "calendar/sync/subscriptions", json=json, params=params)

    def update_subscriptions(self, subscription_id: str, *, json: Any = None, **params: Any) -> Any:
        """Pause, resume, or select an outbound calendar

        ``PATCH /calendar/sync/subscriptions/{subscription_id}``
        """
        return self._c.request("PATCH", f"calendar/sync/subscriptions/{subscription_id}", json=json, params=params)

    def sync_subscriptions(self, subscription_id: str, *, json: Any = None, **params: Any) -> Any:
        """Queue a sync for one subscription

        ``POST /calendar/sync/subscriptions/{subscription_id}/sync``
        """
        return self._c.request("POST", f"calendar/sync/subscriptions/{subscription_id}/sync", json=json, params=params)


class CanvasOps(_Namespace):
    """26 operations."""

    def list_canvas(self, **params: Any) -> Any:
        """List boards

        ``GET /canvas``
        """
        return self._c.request("GET", "canvas", params=params)

    def create_canvas(self, *, json: Any = None, **params: Any) -> Any:
        """Create a board

        ``POST /canvas``
        """
        return self._c.request("POST", "canvas", json=json, params=params)

    def delete_cards(self, card_id: str, **params: Any) -> Any:
        """Remove a card from the board

        ``DELETE /canvas/cards/{card_id}``
        """
        return self._c.request("DELETE", f"canvas/cards/{card_id}", params=params)

    def update_cards(self, card_id: str, *, json: Any = None, **params: Any) -> Any:
        """Move, resize, restyle or edit a card

        ``PATCH /canvas/cards/{card_id}``
        """
        return self._c.request("PATCH", f"canvas/cards/{card_id}", json=json, params=params)

    def get_files(self, card_id: str, file_id: str, **params: Any) -> Any:
        """A file this card shows, from our origin

        ``GET /canvas/cards/{card_id}/files/{file_id}``
        """
        return self._c.request("GET", f"canvas/cards/{card_id}/files/{file_id}", params=params)

    def get_preview_files(self, card_id: str, file_id: str, **params: Any) -> Any:
        """Read a Word document a card shows

        ``GET /canvas/cards/{card_id}/files/{file_id}/preview``
        """
        return self._c.request("GET", f"canvas/cards/{card_id}/files/{file_id}/preview", params=params)

    def get_picture_cards(self, card_id: str, **params: Any) -> Any:
        """A picture card's reduced copy, from our origin

        ``GET /canvas/cards/{card_id}/picture``
        """
        return self._c.request("GET", f"canvas/cards/{card_id}/picture", params=params)

    def get_preview_image_cards(self, card_id: str, **params: Any) -> Any:
        """A link card's preview image, from our origin

        ``GET /canvas/cards/{card_id}/preview-image``
        """
        return self._c.request("GET", f"canvas/cards/{card_id}/preview-image", params=params)

    def ungroup_cards(self, card_id: str, *, json: Any = None, **params: Any) -> Any:
        """Dissolve a group

        ``POST /canvas/cards/{card_id}/ungroup``
        """
        return self._c.request("POST", f"canvas/cards/{card_id}/ungroup", json=json, params=params)

    def delete_connections(self, connection_id: str, **params: Any) -> Any:
        """Remove a connection

        ``DELETE /canvas/connections/{connection_id}``
        """
        return self._c.request("DELETE", f"canvas/connections/{connection_id}", params=params)

    def update_connections(self, connection_id: str, *, json: Any = None, **params: Any) -> Any:
        """Restyle or relabel a connection

        ``PATCH /canvas/connections/{connection_id}``
        """
        return self._c.request("PATCH", f"canvas/connections/{connection_id}", json=json, params=params)

    def delete_canvas(self, canvas_id: str, **params: Any) -> Any:
        """Move a board to trash

        ``DELETE /canvas/{canvas_id}``
        """
        return self._c.request("DELETE", f"canvas/{canvas_id}", params=params)

    def get_canvas(self, canvas_id: str, **params: Any) -> Any:
        """Open a board

        ``GET /canvas/{canvas_id}``
        """
        return self._c.request("GET", f"canvas/{canvas_id}", params=params)

    def update_canvas(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename, move, describe or restore a board

        ``PATCH /canvas/{canvas_id}``
        """
        return self._c.request("PATCH", f"canvas/{canvas_id}", json=json, params=params)

    def delete_cards_canvas(self, canvas_id: str, **params: Any) -> Any:
        """Empty a board

        ``DELETE /canvas/{canvas_id}/cards``
        """
        return self._c.request("DELETE", f"canvas/{canvas_id}/cards", params=params)

    def get_cards_canvas(self, canvas_id: str, **params: Any) -> Any:
        """The cards on a board

        ``GET /canvas/{canvas_id}/cards``
        """
        return self._c.request("GET", f"canvas/{canvas_id}/cards", params=params)

    def cards_canvas(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Put a card on a board

        ``POST /canvas/{canvas_id}/cards``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/cards", json=json, params=params)

    def get_connections_canvas(self, canvas_id: str, **params: Any) -> Any:
        """The lines between cards

        ``GET /canvas/{canvas_id}/connections``
        """
        return self._c.request("GET", f"canvas/{canvas_id}/connections", params=params)

    def connections_canvas(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Connect two cards

        ``POST /canvas/{canvas_id}/connections``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/connections", json=json, params=params)

    def duplicate_canvas(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Copy a board - every card, group and line, as a new board

        ``POST /canvas/{canvas_id}/duplicate``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/duplicate", json=json, params=params)

    def group_canvas(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Group several cards into a named section

        ``POST /canvas/{canvas_id}/group``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/group", json=json, params=params)

    def delete_items(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Delete several cards and lines in one call

        ``POST /canvas/{canvas_id}/items/delete``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/items/delete", json=json, params=params)

    def restore_items(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Restore deleted cards and lines as themselves

        ``POST /canvas/{canvas_id}/items/restore``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/items/restore", json=json, params=params)

    def purge_canvas(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Permanently delete a board that is in Trash

        ``POST /canvas/{canvas_id}/purge``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/purge", json=json, params=params)

    def section_members_canvas(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Move cards into a section, or out of one

        ``POST /canvas/{canvas_id}/section-members``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/section-members", json=json, params=params)

    def upload_folder_canvas(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Where this board's uploads are filed

        ``POST /canvas/{canvas_id}/upload-folder``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/upload-folder", json=json, params=params)


class CollabOps(_Namespace):
    """127 operations."""

    def create_messages(self, *, json: Any = None, **params: Any) -> Any:
        """An app writes to its person

        ``POST /collab/app-dm/messages``
        """
        return self._c.request("POST", "collab/app-dm/messages", json=json, params=params)

    def get_content_attachments(self, attachment_id: str, **params: Any) -> Any:
        """Open a posted file

        ``GET /collab/attachments/{attachment_id}/content``
        """
        return self._c.request("GET", f"collab/attachments/{attachment_id}/content", params=params)

    def save_attachments(self, attachment_id: str, *, json: Any = None, **params: Any) -> Any:
        """Keep a copy of a file from a chat you are in

        ``POST /collab/attachments/{attachment_id}/save``
        """
        return self._c.request("POST", f"collab/attachments/{attachment_id}/save", json=json, params=params)

    def get_text_attachments(self, attachment_id: str, **params: Any) -> Any:
        """Read a posted note

        ``GET /collab/attachments/{attachment_id}/text``
        """
        return self._c.request("GET", f"collab/attachments/{attachment_id}/text", params=params)

    def list_blocks(self, **params: Any) -> Any:
        """People you blocked

        ``GET /collab/blocks``
        """
        return self._c.request("GET", "collab/blocks", params=params)

    def create_blocks(self, *, json: Any = None, **params: Any) -> Any:
        """Block someone

        ``POST /collab/blocks``
        """
        return self._c.request("POST", "collab/blocks", json=json, params=params)

    def delete_blocks(self, user_id: str, **params: Any) -> Any:
        """Unblock someone

        ``DELETE /collab/blocks/{user_id}``
        """
        return self._c.request("DELETE", f"collab/blocks/{user_id}", params=params)

    def list_ringing(self, **params: Any) -> Any:
        """The calls ringing for you now

        ``GET /collab/calls/ringing``
        """
        return self._c.request("GET", "collab/calls/ringing", params=params)

    def list_trending(self, **params: Any) -> Any:
        """Public channels busiest this week

        ``GET /collab/channels/trending``
        """
        return self._c.request("GET", "collab/channels/trending", params=params)

    def list_chat_files(self, **params: Any) -> Any:
        """Files from the chats you are in

        ``GET /collab/chat-files``
        """
        return self._c.request("GET", "collab/chat-files", params=params)

    def list_conversations(self, **params: Any) -> Any:
        """Your conversations

        ``GET /collab/conversations``
        """
        return self._c.request("GET", "collab/conversations", params=params)

    def create_conversations(self, *, json: Any = None, **params: Any) -> Any:
        """Create a channel or group chat, or open a DM

        ``POST /collab/conversations``
        """
        return self._c.request("POST", "collab/conversations", json=json, params=params)

    def list_trash(self, **params: Any) -> Any:
        """Deleted conversations you can restore

        ``GET /collab/conversations/trash``
        """
        return self._c.request("GET", "collab/conversations/trash", params=params)

    def delete_conversations(self, conv_id: str, **params: Any) -> Any:
        """Delete a channel or group chat

        ``DELETE /collab/conversations/{conv_id}``
        """
        return self._c.request("DELETE", f"collab/conversations/{conv_id}", params=params)

    def get_conversations(self, conv_id: str, **params: Any) -> Any:
        """One conversation

        ``GET /collab/conversations/{conv_id}``
        """
        return self._c.request("GET", f"collab/conversations/{conv_id}", params=params)

    def update_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change a conversation, or your notifications for it

        ``PATCH /collab/conversations/{conv_id}``
        """
        return self._c.request("PATCH", f"collab/conversations/{conv_id}", json=json, params=params)

    def archive_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Archive

        ``POST /collab/conversations/{conv_id}/archive``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/archive", json=json, params=params)

    def get_files_conversations(self, conv_id: str, **params: Any) -> Any:
        """The conversation's files

        ``GET /collab/conversations/{conv_id}/files``
        """
        return self._c.request("GET", f"collab/conversations/{conv_id}/files", params=params)

    def join_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Join

        ``POST /collab/conversations/{conv_id}/join``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/join", json=json, params=params)

    def get_join_requests_conversations(self, conv_id: str, **params: Any) -> Any:
        """Requests to join

        ``GET /collab/conversations/{conv_id}/join-requests``
        """
        return self._c.request("GET", f"collab/conversations/{conv_id}/join-requests", params=params)

    def approve_join_requests(self, conv_id: str, request_id: str, *, json: Any = None, **params: Any) -> Any:
        """Approve a request to join

        ``POST /collab/conversations/{conv_id}/join-requests/{request_id}/approve``
        """
        return self._c.request(
            "POST", f"collab/conversations/{conv_id}/join-requests/{request_id}/approve", json=json, params=params
        )

    def decline_join_requests(self, conv_id: str, request_id: str, *, json: Any = None, **params: Any) -> Any:
        """Decline a request to join

        ``POST /collab/conversations/{conv_id}/join-requests/{request_id}/decline``
        """
        return self._c.request(
            "POST", f"collab/conversations/{conv_id}/join-requests/{request_id}/decline", json=json, params=params
        )

    def leave_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Leave

        ``POST /collab/conversations/{conv_id}/leave``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/leave", json=json, params=params)

    def get_link_conversations(self, conv_id: str, **params: Any) -> Any:
        """The channel's link

        ``GET /collab/conversations/{conv_id}/link``
        """
        return self._c.request("GET", f"collab/conversations/{conv_id}/link", params=params)

    def link_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Replace the channel's link

        ``POST /collab/conversations/{conv_id}/link``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/link", json=json, params=params)

    def meetings_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Start a meeting or call here

        ``POST /collab/conversations/{conv_id}/meetings``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/meetings", json=json, params=params)

    def get_members_conversations(self, conv_id: str, **params: Any) -> Any:
        """Who is in it

        ``GET /collab/conversations/{conv_id}/members``
        """
        return self._c.request("GET", f"collab/conversations/{conv_id}/members", params=params)

    def members_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Add people

        ``POST /collab/conversations/{conv_id}/members``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/members", json=json, params=params)

    def delete_members(self, conv_id: str, user_id: str, **params: Any) -> Any:
        """Remove someone

        ``DELETE /collab/conversations/{conv_id}/members/{user_id}``
        """
        return self._c.request("DELETE", f"collab/conversations/{conv_id}/members/{user_id}", params=params)

    def update_members(self, conv_id: str, user_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change someone's role, lift a ban, or share the history with them

        ``PATCH /collab/conversations/{conv_id}/members/{user_id}``
        """
        return self._c.request("PATCH", f"collab/conversations/{conv_id}/members/{user_id}", json=json, params=params)

    def get_messages_conversations(self, conv_id: str, **params: Any) -> Any:
        """Messages, newest first

        ``GET /collab/conversations/{conv_id}/messages``
        """
        return self._c.request("GET", f"collab/conversations/{conv_id}/messages", params=params)

    def messages_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Send a message

        ``POST /collab/conversations/{conv_id}/messages``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/messages", json=json, params=params)

    def update_personal_ai_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """AI search in one personal chat

        ``PATCH /collab/conversations/{conv_id}/personal-ai``
        """
        return self._c.request("PATCH", f"collab/conversations/{conv_id}/personal-ai", json=json, params=params)

    def resume_personal_ai(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Resume paused AI search in a personal chat

        ``POST /collab/conversations/{conv_id}/personal-ai/resume``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/personal-ai/resume", json=json, params=params)

    def delete_pin_conversations(self, conv_id: str, **params: Any) -> Any:
        """Unpin a conversation

        ``DELETE /collab/conversations/{conv_id}/pin``
        """
        return self._c.request("DELETE", f"collab/conversations/{conv_id}/pin", params=params)

    def pin_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Pin a conversation

        ``POST /collab/conversations/{conv_id}/pin``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/pin", json=json, params=params)

    def get_pins_conversations(self, conv_id: str, **params: Any) -> Any:
        """Pinned messages

        ``GET /collab/conversations/{conv_id}/pins``
        """
        return self._c.request("GET", f"collab/conversations/{conv_id}/pins", params=params)

    def read_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Mark as read

        ``POST /collab/conversations/{conv_id}/read``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/read", json=json, params=params)

    def get_reports_conversations(self, conv_id: str, **params: Any) -> Any:
        """Reports for the moderators

        ``GET /collab/conversations/{conv_id}/reports``
        """
        return self._c.request("GET", f"collab/conversations/{conv_id}/reports", params=params)

    def delete_message_reports(self, conv_id: str, report_id: str, *, json: Any = None, **params: Any) -> Any:
        """Delete the reported message

        ``POST /collab/conversations/{conv_id}/reports/{report_id}/delete-message``
        """
        return self._c.request(
            "POST", f"collab/conversations/{conv_id}/reports/{report_id}/delete-message", json=json, params=params
        )

    def dismiss_reports(self, conv_id: str, report_id: str, *, json: Any = None, **params: Any) -> Any:
        """Dismiss a report

        ``POST /collab/conversations/{conv_id}/reports/{report_id}/dismiss``
        """
        return self._c.request(
            "POST", f"collab/conversations/{conv_id}/reports/{report_id}/dismiss", json=json, params=params
        )

    def remove_person_reports(self, conv_id: str, report_id: str, *, json: Any = None, **params: Any) -> Any:
        """Remove the reported person

        ``POST /collab/conversations/{conv_id}/reports/{report_id}/remove-person``
        """
        return self._c.request(
            "POST", f"collab/conversations/{conv_id}/reports/{report_id}/remove-person", json=json, params=params
        )

    def restore_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Restore from Trash

        ``POST /collab/conversations/{conv_id}/restore``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/restore", json=json, params=params)

    def typing_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """You are typing here

        ``POST /collab/conversations/{conv_id}/typing``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/typing", json=json, params=params)

    def unarchive_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Unarchive

        ``POST /collab/conversations/{conv_id}/unarchive``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/unarchive", json=json, params=params)

    def upload_folder_conversations(self, conv_id: str, *, json: Any = None, **params: Any) -> Any:
        """Where an upload in a channel goes

        ``POST /collab/conversations/{conv_id}/upload-folder``
        """
        return self._c.request("POST", f"collab/conversations/{conv_id}/upload-folder", json=json, params=params)

    def meeting_events(self, event_id: str, *, json: Any = None, **params: Any) -> Any:
        """Open the meeting on a calendar event

        ``POST /collab/events/{event_id}/meeting``
        """
        return self._c.request("POST", f"collab/events/{event_id}/meeting", json=json, params=params)

    def list_held_files(self, **params: Any) -> Any:
        """Chat files you hold for a former member

        ``GET /collab/held-files``
        """
        return self._c.request("GET", "collab/held-files", params=params)

    def delete_held_files(self, file_id: str, **params: Any) -> Any:
        """Delete a held chat file for good

        ``DELETE /collab/held-files/{file_id}``
        """
        return self._c.request("DELETE", f"collab/held-files/{file_id}", params=params)

    def give_held_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Give a held chat file to someone in its chat

        ``POST /collab/held-files/{file_id}/give``
        """
        return self._c.request("POST", f"collab/held-files/{file_id}/give", json=json, params=params)

    def get_join(self, token: str, **params: Any) -> Any:
        """What a channel link opens

        ``GET /collab/join/{token}``
        """
        return self._c.request("GET", f"collab/join/{token}", params=params)

    def create_join(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Join through a channel link

        ``POST /collab/join/{token}``
        """
        return self._c.request("POST", f"collab/join/{token}", json=json, params=params)

    def list_live_calls(self, **params: Any) -> Any:
        """The calendar calls on now in this space

        ``GET /collab/live-calls``
        """
        return self._c.request("GET", "collab/live-calls", params=params)

    def create_live_pass(self, *, json: Any = None, **params: Any) -> Any:
        """A pass for your live channel

        ``POST /collab/live-pass``
        """
        return self._c.request("POST", "collab/live-pass", json=json, params=params)

    def get_meet(self, token: str, **params: Any) -> Any:
        """A meeting from its guest link

        ``GET /collab/meet/{token}``
        """
        return self._c.request("GET", f"collab/meet/{token}", params=params)

    def delete_ask_meet(self, token: str, **params: Any) -> Any:
        """Stop waiting, as a guest

        ``DELETE /collab/meet/{token}/ask``
        """
        return self._c.request("DELETE", f"collab/meet/{token}/ask", params=params)

    def ask_meet(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Ask to join, as a guest

        ``POST /collab/meet/{token}/ask``
        """
        return self._c.request("POST", f"collab/meet/{token}/ask", json=json, params=params)

    def get_chat_meet(self, token: str, **params: Any) -> Any:
        """The meeting chat, as a guest

        ``GET /collab/meet/{token}/chat``
        """
        return self._c.request("GET", f"collab/meet/{token}/chat", params=params)

    def chat_meet(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Write in the meeting chat, as a guest

        ``POST /collab/meet/{token}/chat``
        """
        return self._c.request("POST", f"collab/meet/{token}/chat", json=json, params=params)

    def get_attachments(self, token: str, attachment_id: str, **params: Any) -> Any:
        """Open a file from the meeting chat, as a guest

        ``GET /collab/meet/{token}/chat/attachments/{attachment_id}``
        """
        return self._c.request("GET", f"collab/meet/{token}/chat/attachments/{attachment_id}", params=params)

    def files_chat(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Put a file in the meeting chat, as a guest

        ``POST /collab/meet/{token}/chat/files``
        """
        return self._c.request("POST", f"collab/meet/{token}/chat/files", json=json, params=params)

    def enter_meet(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Go in, once a host admitted you

        ``POST /collab/meet/{token}/enter``
        """
        return self._c.request("POST", f"collab/meet/{token}/enter", json=json, params=params)

    def leave_meet(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Leave, as a guest

        ``POST /collab/meet/{token}/leave``
        """
        return self._c.request("POST", f"collab/meet/{token}/leave", json=json, params=params)

    def update_me_meet(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Your microphone, camera, screen and hand, as a guest

        ``PATCH /collab/meet/{token}/me``
        """
        return self._c.request("PATCH", f"collab/meet/{token}/me", json=json, params=params)

    def quality_meet(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Report call quality, as a guest

        ``POST /collab/meet/{token}/quality``
        """
        return self._c.request("POST", f"collab/meet/{token}/quality", json=json, params=params)

    def state_meet(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """The meeting now, as a guest (and your heartbeat)

        ``POST /collab/meet/{token}/state``
        """
        return self._c.request("POST", f"collab/meet/{token}/state", json=json, params=params)

    def get_meetings(self, meeting_id: str, **params: Any) -> Any:
        """A meeting, before joining

        ``GET /collab/meetings/{meeting_id}``
        """
        return self._c.request("GET", f"collab/meetings/{meeting_id}", params=params)

    def update_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Set the meeting's spoken language

        ``PATCH /collab/meetings/{meeting_id}``
        """
        return self._c.request("PATCH", f"collab/meetings/{meeting_id}", json=json, params=params)

    def answer_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Answer a call ringing for you

        ``POST /collab/meetings/{meeting_id}/answer``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/answer", json=json, params=params)

    def delete_ask_meetings(self, meeting_id: str, **params: Any) -> Any:
        """Stop waiting in the lobby

        ``DELETE /collab/meetings/{meeting_id}/ask``
        """
        return self._c.request("DELETE", f"collab/meetings/{meeting_id}/ask", params=params)

    def capture_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Turn recording or transcription on or off

        ``POST /collab/meetings/{meeting_id}/capture``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/capture", json=json, params=params)

    def get_chat_meetings(self, meeting_id: str, **params: Any) -> Any:
        """The meeting chat

        ``GET /collab/meetings/{meeting_id}/chat``
        """
        return self._c.request("GET", f"collab/meetings/{meeting_id}/chat", params=params)

    def chat_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Write in the meeting chat

        ``POST /collab/meetings/{meeting_id}/chat``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/chat", json=json, params=params)

    def get_chat_attachments(self, meeting_id: str, attachment_id: str, **params: Any) -> Any:
        """Open a file from the meeting chat

        ``GET /collab/meetings/{meeting_id}/chat/attachments/{attachment_id}``
        """
        return self._c.request("GET", f"collab/meetings/{meeting_id}/chat/attachments/{attachment_id}", params=params)

    def files_meetings_chat(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Put a file in the meeting chat

        ``POST /collab/meetings/{meeting_id}/chat/files``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/chat/files", json=json, params=params)

    def end_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """End for everyone

        ``POST /collab/meetings/{meeting_id}/end``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/end", json=json, params=params)

    def join_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Go in, or ask to

        ``POST /collab/meetings/{meeting_id}/join``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/join", json=json, params=params)

    def leave_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Leave

        ``POST /collab/meetings/{meeting_id}/leave``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/leave", json=json, params=params)

    def link_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Make a new guest link

        ``POST /collab/meetings/{meeting_id}/link``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/link", json=json, params=params)

    def update_me_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Your microphone, camera, screen and hand

        ``PATCH /collab/meetings/{meeting_id}/me``
        """
        return self._c.request("PATCH", f"collab/meetings/{meeting_id}/me", json=json, params=params)

    def mute_all_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Mute everyone else

        ``POST /collab/meetings/{meeting_id}/mute-all``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/mute-all", json=json, params=params)

    def admit_participants(self, meeting_id: str, participant_id: str, *, json: Any = None, **params: Any) -> Any:
        """Admit someone from the lobby

        ``POST /collab/meetings/{meeting_id}/participants/{participant_id}/admit``
        """
        return self._c.request(
            "POST", f"collab/meetings/{meeting_id}/participants/{participant_id}/admit", json=json, params=params
        )

    def deny_participants(self, meeting_id: str, participant_id: str, *, json: Any = None, **params: Any) -> Any:
        """Turn down a lobby request

        ``POST /collab/meetings/{meeting_id}/participants/{participant_id}/deny``
        """
        return self._c.request(
            "POST", f"collab/meetings/{meeting_id}/participants/{participant_id}/deny", json=json, params=params
        )

    def lower_hand_participants(self, meeting_id: str, participant_id: str, *, json: Any = None, **params: Any) -> Any:
        """Lower someone's hand

        ``POST /collab/meetings/{meeting_id}/participants/{participant_id}/lower-hand``
        """
        return self._c.request(
            "POST", f"collab/meetings/{meeting_id}/participants/{participant_id}/lower-hand", json=json, params=params
        )

    def make_host_participants(self, meeting_id: str, participant_id: str, *, json: Any = None, **params: Any) -> Any:
        """Make someone a host

        ``POST /collab/meetings/{meeting_id}/participants/{participant_id}/make-host``
        """
        return self._c.request(
            "POST", f"collab/meetings/{meeting_id}/participants/{participant_id}/make-host", json=json, params=params
        )

    def mute_participants(self, meeting_id: str, participant_id: str, *, json: Any = None, **params: Any) -> Any:
        """Mute someone

        ``POST /collab/meetings/{meeting_id}/participants/{participant_id}/mute``
        """
        return self._c.request(
            "POST", f"collab/meetings/{meeting_id}/participants/{participant_id}/mute", json=json, params=params
        )

    def remove_participants(self, meeting_id: str, participant_id: str, *, json: Any = None, **params: Any) -> Any:
        """Remove someone from the meeting

        ``POST /collab/meetings/{meeting_id}/participants/{participant_id}/remove``
        """
        return self._c.request(
            "POST", f"collab/meetings/{meeting_id}/participants/{participant_id}/remove", json=json, params=params
        )

    def get_quality_meetings(self, meeting_id: str, **params: Any) -> Any:
        """Attendees' recent call quality, for hosts

        ``GET /collab/meetings/{meeting_id}/quality``
        """
        return self._c.request("GET", f"collab/meetings/{meeting_id}/quality", params=params)

    def quality_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """Report call quality

        ``POST /collab/meetings/{meeting_id}/quality``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/quality", json=json, params=params)

    def state_meetings(self, meeting_id: str, *, json: Any = None, **params: Any) -> Any:
        """The meeting now (and your heartbeat)

        ``POST /collab/meetings/{meeting_id}/state``
        """
        return self._c.request("POST", f"collab/meetings/{meeting_id}/state", json=json, params=params)

    def list_mentions(self, **params: Any) -> Any:
        """The Mentions tab

        ``GET /collab/mentions``
        """
        return self._c.request("GET", "collab/mentions", params=params)

    def delete_messages(self, message_id: str, **params: Any) -> Any:
        """Delete a message

        ``DELETE /collab/messages/{message_id}``
        """
        return self._c.request("DELETE", f"collab/messages/{message_id}", params=params)

    def get_messages(self, message_id: str, **params: Any) -> Any:
        """One message

        ``GET /collab/messages/{message_id}``
        """
        return self._c.request("GET", f"collab/messages/{message_id}", params=params)

    def update_messages(self, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Edit your message

        ``PATCH /collab/messages/{message_id}``
        """
        return self._c.request("PATCH", f"collab/messages/{message_id}", json=json, params=params)

    def delete_follow_messages(self, message_id: str, **params: Any) -> Any:
        """Unfollow a thread

        ``DELETE /collab/messages/{message_id}/follow``
        """
        return self._c.request("DELETE", f"collab/messages/{message_id}/follow", params=params)

    def follow_messages(self, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Follow a thread

        ``POST /collab/messages/{message_id}/follow``
        """
        return self._c.request("POST", f"collab/messages/{message_id}/follow", json=json, params=params)

    def forward_messages(self, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Forward a message to another chat

        ``POST /collab/messages/{message_id}/forward``
        """
        return self._c.request("POST", f"collab/messages/{message_id}/forward", json=json, params=params)

    def delete_pin_messages(self, message_id: str, **params: Any) -> Any:
        """Unpin

        ``DELETE /collab/messages/{message_id}/pin``
        """
        return self._c.request("DELETE", f"collab/messages/{message_id}/pin", params=params)

    def pin_messages(self, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Pin

        ``POST /collab/messages/{message_id}/pin``
        """
        return self._c.request("POST", f"collab/messages/{message_id}/pin", json=json, params=params)

    def delete_reactions_messages(self, message_id: str, **params: Any) -> Any:
        """Take a reaction back

        ``DELETE /collab/messages/{message_id}/reactions``
        """
        return self._c.request("DELETE", f"collab/messages/{message_id}/reactions", params=params)

    def reactions_messages(self, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """React

        ``POST /collab/messages/{message_id}/reactions``
        """
        return self._c.request("POST", f"collab/messages/{message_id}/reactions", json=json, params=params)

    def recap_tasks_messages(self, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Add a meeting's action items as tasks

        ``POST /collab/messages/{message_id}/recap-tasks``
        """
        return self._c.request("POST", f"collab/messages/{message_id}/recap-tasks", json=json, params=params)

    def get_replies_messages(self, message_id: str, **params: Any) -> Any:
        """A thread

        ``GET /collab/messages/{message_id}/replies``
        """
        return self._c.request("GET", f"collab/messages/{message_id}/replies", params=params)

    def list_mutes(self, **params: Any) -> Any:
        """People you muted

        ``GET /collab/mutes``
        """
        return self._c.request("GET", "collab/mutes", params=params)

    def create_mutes(self, *, json: Any = None, **params: Any) -> Any:
        """Mute someone

        ``POST /collab/mutes``
        """
        return self._c.request("POST", "collab/mutes", json=json, params=params)

    def delete_mutes(self, user_id: str, **params: Any) -> Any:
        """Unmute someone

        ``DELETE /collab/mutes/{user_id}``
        """
        return self._c.request("DELETE", f"collab/mutes/{user_id}", params=params)

    def list_owned_public_channels(self, **params: Any) -> Any:
        """Public channels someone owns in a workspace

        ``GET /collab/owned-public-channels``
        """
        return self._c.request("GET", "collab/owned-public-channels", params=params)

    def list_people(self, **params: Any) -> Any:
        """Who you can message here

        ``GET /collab/people``
        """
        return self._c.request("GET", "collab/people", params=params)

    def list_personal_ai(self, **params: Any) -> Any:
        """Your setting for AI search over personal chats

        ``GET /collab/personal-ai``
        """
        return self._c.request("GET", "collab/personal-ai", params=params)

    def update_personal_ai(self, *, json: Any = None, **params: Any) -> Any:
        """Turn AI search over your personal chats on or off

        ``PATCH /collab/personal-ai``
        """
        return self._c.request("PATCH", "collab/personal-ai", json=json, params=params)

    def update_pinned(self, *, json: Any = None, **params: Any) -> Any:
        """Put your pinned conversations in order

        ``PUT /collab/pinned``
        """
        return self._c.request("PUT", "collab/pinned", json=json, params=params)

    def list_presence(self, **params: Any) -> Any:
        """Who is online

        ``GET /collab/presence``
        """
        return self._c.request("GET", "collab/presence", params=params)

    def create_presence(self, *, json: Any = None, **params: Any) -> Any:
        """A beat from an open tab

        ``POST /collab/presence``
        """
        return self._c.request("POST", "collab/presence", json=json, params=params)

    def list_me(self, **params: Any) -> Any:
        """Your status and status privacy

        ``GET /collab/presence/me``
        """
        return self._c.request("GET", "collab/presence/me", params=params)

    def update_me(self, *, json: Any = None, **params: Any) -> Any:
        """Set your status or status privacy

        ``PATCH /collab/presence/me``
        """
        return self._c.request("PATCH", "collab/presence/me", json=json, params=params)

    def list_public_channels(self, **params: Any) -> Any:
        """Browse public channels

        ``GET /collab/public-channels``
        """
        return self._c.request("GET", "collab/public-channels", params=params)

    def list_reach(self, **params: Any) -> Any:
        """Find someone by username, and what you can do

        ``GET /collab/reach``
        """
        return self._c.request("GET", "collab/reach", params=params)

    def create_reports(self, *, json: Any = None, **params: Any) -> Any:
        """Report someone to FlowpyDisk

        ``POST /collab/reports``
        """
        return self._c.request("POST", "collab/reports", json=json, params=params)

    def list_requests(self, **params: Any) -> Any:
        """Message requests and group invites waiting for you

        ``GET /collab/requests``
        """
        return self._c.request("GET", "collab/requests", params=params)

    def accept_requests(self, request_id: str, *, json: Any = None, **params: Any) -> Any:
        """Accept a request

        ``POST /collab/requests/{request_id}/accept``
        """
        return self._c.request("POST", f"collab/requests/{request_id}/accept", json=json, params=params)

    def ignore_requests(self, request_id: str, *, json: Any = None, **params: Any) -> Any:
        """Ignore a request

        ``POST /collab/requests/{request_id}/ignore``
        """
        return self._c.request("POST", f"collab/requests/{request_id}/ignore", json=json, params=params)

    def list_search(self, **params: Any) -> Any:
        """Search Collab

        ``GET /collab/search``
        """
        return self._c.request("GET", "collab/search", params=params)

    def list_threads(self, **params: Any) -> Any:
        """Your threads

        ``GET /collab/threads``
        """
        return self._c.request("GET", "collab/threads", params=params)

    def list_unread(self, **params: Any) -> Any:
        """What waits for you

        ``GET /collab/unread``
        """
        return self._c.request("GET", "collab/unread", params=params)

    def list_spaces(self, **params: Any) -> Any:
        """What waits in each of your spaces

        ``GET /collab/unread/spaces``
        """
        return self._c.request("GET", "collab/unread/spaces", params=params)

    def get_settings_workspaces(self, workspace_id: str, **params: Any) -> Any:
        """A workspace's Collab settings

        ``GET /collab/workspaces/{workspace_id}/settings``
        """
        return self._c.request("GET", f"collab/workspaces/{workspace_id}/settings", params=params)

    def update_settings_workspaces(self, workspace_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change a workspace's Collab settings

        ``PATCH /collab/workspaces/{workspace_id}/settings``
        """
        return self._c.request("PATCH", f"collab/workspaces/{workspace_id}/settings", json=json, params=params)


class CommentsOps(_Namespace):
    """5 operations."""

    def list_comments(self, **params: Any) -> Any:
        """Comments on one file, table or canvas

        ``GET /comments``
        """
        return self._c.request("GET", "comments", params=params)

    def create_comments(self, *, json: Any = None, **params: Any) -> Any:
        """Comment on a file

        ``POST /comments``
        """
        return self._c.request("POST", "comments", json=json, params=params)

    def list_mentionable(self, **params: Any) -> Any:
        """Who can be @mentioned on this file, table or canvas

        ``GET /comments/mentionable``
        """
        return self._c.request("GET", "comments/mentionable", params=params)

    def delete_comments(self, comment_id: str, **params: Any) -> Any:
        """Delete your own comment

        ``DELETE /comments/{comment_id}``
        """
        return self._c.request("DELETE", f"comments/{comment_id}", params=params)

    def update_comments(self, comment_id: str, *, json: Any = None, **params: Any) -> Any:
        """Edit your own comment, or resolve a thread

        ``PATCH /comments/{comment_id}``
        """
        return self._c.request("PATCH", f"comments/{comment_id}", json=json, params=params)


class ConnectionsOps(_Namespace):
    """1 operations."""

    def create_events(self, *, json: Any = None, **params: Any) -> Any:
        """Composio trigger events (Composio only)

        ``POST /connections/composio/events``
        """
        return self._c.request("POST", "connections/composio/events", json=json, params=params)


class DriveImportsOps(_Namespace):
    """5 operations."""

    def list_drive_imports(self, **params: Any) -> Any:
        """List your moves

        ``GET /drive-imports/``
        """
        return self._c.request("GET", "drive-imports/", params=params)

    def list_sources(self, **params: Any) -> Any:
        """The drives files can be moved in from

        ``GET /drive-imports/sources``
        """
        return self._c.request("GET", "drive-imports/sources", params=params)

    def get_drive_imports(self, import_id: str, **params: Any) -> Any:
        """Read a move (its scan and progress)

        ``GET /drive-imports/{import_id}``
        """
        return self._c.request("GET", f"drive-imports/{import_id}", params=params)

    def get_items_drive_imports(self, import_id: str, **params: Any) -> Any:
        """List a move's files

        ``GET /drive-imports/{import_id}/items``
        """
        return self._c.request("GET", f"drive-imports/{import_id}/items", params=params)

    def get_report_drive_imports(self, import_id: str, **params: Any) -> Any:
        """A move's report

        ``GET /drive-imports/{import_id}/report``
        """
        return self._c.request("GET", f"drive-imports/{import_id}/report", params=params)


class FormsOps(_Namespace):
    """14 operations."""

    def list_forms(self, **params: Any) -> Any:
        """List your forms

        ``GET /forms``
        """
        return self._c.request("GET", "forms", params=params)

    def create_forms(self, *, json: Any = None, **params: Any) -> Any:
        """Create a form

        ``POST /forms``
        """
        return self._c.request("POST", "forms", json=json, params=params)

    def list_reference(self, **params: Any) -> Any:
        """The country and currency lists a builder fills its pickers from

        ``GET /forms/reference``
        """
        return self._c.request("GET", "forms/reference", params=params)

    def delete_forms(self, form_id: str, **params: Any) -> Any:
        """Move a form to the trash

        ``DELETE /forms/{form_id}``
        """
        return self._c.request("DELETE", f"forms/{form_id}", params=params)

    def get_forms(self, form_id: str, **params: Any) -> Any:
        """A form with its questions

        ``GET /forms/{form_id}``
        """
        return self._c.request("GET", f"forms/{form_id}", params=params)

    def update_forms(self, form_id: str, *, json: Any = None, **params: Any) -> Any:
        """Edit a form

        ``PATCH /forms/{form_id}``
        """
        return self._c.request("PATCH", f"forms/{form_id}", json=json, params=params)

    def duplicate_forms(self, form_id: str, *, json: Any = None, **params: Any) -> Any:
        """Copy a form - the same questions, none of the answers

        ``POST /forms/{form_id}/duplicate``
        """
        return self._c.request("POST", f"forms/{form_id}/duplicate", json=json, params=params)

    def purge_forms(self, form_id: str, *, json: Any = None, **params: Any) -> Any:
        """Delete a trashed form permanently

        ``POST /forms/{form_id}/purge``
        """
        return self._c.request("POST", f"forms/{form_id}/purge", json=json, params=params)

    def get_questions_forms(self, form_id: str, **params: Any) -> Any:
        """The questions, in order

        ``GET /forms/{form_id}/questions``
        """
        return self._c.request("GET", f"forms/{form_id}/questions", params=params)

    def questions_forms(self, form_id: str, *, json: Any = None, **params: Any) -> Any:
        """Add a question (or a layout block)

        ``POST /forms/{form_id}/questions``
        """
        return self._c.request("POST", f"forms/{form_id}/questions", json=json, params=params)

    def reorder_questions(self, form_id: str, *, json: Any = None, **params: Any) -> Any:
        """Reorder the questions

        ``POST /forms/{form_id}/questions/reorder``
        """
        return self._c.request("POST", f"forms/{form_id}/questions/reorder", json=json, params=params)

    def delete_questions(self, form_id: str, question_id: str, **params: Any) -> Any:
        """Remove a question

        ``DELETE /forms/{form_id}/questions/{question_id}``
        """
        return self._c.request("DELETE", f"forms/{form_id}/questions/{question_id}", params=params)

    def update_questions(self, form_id: str, question_id: str, *, json: Any = None, **params: Any) -> Any:
        """Edit a question

        ``PATCH /forms/{form_id}/questions/{question_id}``
        """
        return self._c.request("PATCH", f"forms/{form_id}/questions/{question_id}", json=json, params=params)

    def get_responses_forms(self, form_id: str, **params: Any) -> Any:
        """The answers, read through to the form's table

        ``GET /forms/{form_id}/responses``
        """
        return self._c.request("GET", f"forms/{form_id}/responses", params=params)


class GraphOps(_Namespace):
    """6 operations."""

    def list_graph(self, **params: Any) -> Any:
        """The knowledge graph you can see, as GraphRAG-ready graph.json

        ``GET /graph``
        """
        return self._c.request("GET", "graph", params=params)

    def list_around(self, **params: Any) -> Any:
        """One item and what is around it

        ``GET /graph/around``
        """
        return self._c.request("GET", "graph/around", params=params)

    def get_mentions(self, file_id: str, **params: Any) -> Any:
        """Backlinks - who mentions this file, linked and unlinked

        ``GET /graph/mentions/{file_id}``
        """
        return self._c.request("GET", f"graph/mentions/{file_id}", params=params)

    def create_rebuild(self, *, json: Any = None, **params: Any) -> Any:
        """Force a full rebuild of your graph

        ``POST /graph/rebuild``
        """
        return self._c.request("POST", "graph/rebuild", json=json, params=params)

    def get_related(self, file_id: str, **params: Any) -> Any:
        """What relates to this file

        ``GET /graph/related/{file_id}``
        """
        return self._c.request("GET", f"graph/related/{file_id}", params=params)

    def list_search(self, **params: Any) -> Any:
        """Graph-aware search - matches plus their neighbours

        ``GET /graph/search``
        """
        return self._c.request("GET", "graph/search", params=params)


class InboundWebhooksOps(_Namespace):
    """8 operations."""

    def list_inbound_webhooks(self, **params: Any) -> Any:
        """List incoming endpoints in the acting workspace

        ``GET /inbound-webhooks/``
        """
        return self._c.request("GET", "inbound-webhooks/", params=params)

    def create_v1(self, endpoint_id: str, *, json: Any = None, **params: Any) -> Any:
        """Deliver one signed creation request

        ``POST /inbound-webhooks/v1/{endpoint_id}``
        """
        return self._c.request("POST", f"inbound-webhooks/v1/{endpoint_id}", json=json, params=params)

    def get_inbound_webhooks(self, endpoint_id: str, **params: Any) -> Any:
        """Read incoming endpoint metadata

        ``GET /inbound-webhooks/{endpoint_id}/``
        """
        return self._c.request("GET", f"inbound-webhooks/{endpoint_id}/", params=params)

    def get_receipts_inbound_webhooks(self, endpoint_id: str, **params: Any) -> Any:
        """Read payload-free delivery history

        ``GET /inbound-webhooks/{endpoint_id}/receipts/``
        """
        return self._c.request("GET", f"inbound-webhooks/{endpoint_id}/receipts/", params=params)

    def abort_uploads(self, endpoint_id: str, session_id: str, *, json: Any = None, **params: Any) -> Any:
        """Abort one pending signed file upload

        ``POST /inbound-webhooks/{endpoint_id}/uploads/{session_id}/abort``
        """
        return self._c.request(
            "POST", f"inbound-webhooks/{endpoint_id}/uploads/{session_id}/abort", json=json, params=params
        )

    def complete_uploads(self, endpoint_id: str, session_id: str, *, json: Any = None, **params: Any) -> Any:
        """Complete one signed file upload

        ``POST /inbound-webhooks/{endpoint_id}/uploads/{session_id}/complete``
        """
        return self._c.request(
            "POST", f"inbound-webhooks/{endpoint_id}/uploads/{session_id}/complete", json=json, params=params
        )

    def parts_uploads(self, endpoint_id: str, session_id: str, *, json: Any = None, **params: Any) -> Any:
        """Get a scoped upload URL for one part

        ``POST /inbound-webhooks/{endpoint_id}/uploads/{session_id}/parts``
        """
        return self._c.request(
            "POST", f"inbound-webhooks/{endpoint_id}/uploads/{session_id}/parts", json=json, params=params
        )

    def update_bytes_parts(
        self, endpoint_id: str, session_id: str, part_number: str, *, json: Any = None, **params: Any
    ) -> Any:
        """Upload bytes to a local-storage part URL

        ``PUT /inbound-webhooks/{endpoint_id}/uploads/{session_id}/parts/{part_number}/bytes``
        """
        return self._c.request(
            "PUT",
            f"inbound-webhooks/{endpoint_id}/uploads/{session_id}/parts/{part_number}/bytes",
            json=json,
            params=params,
        )


class InsightsOps(_Namespace):
    """2 operations."""

    def list_background_work(self, **params: Any) -> Any:
        """What was indexed for the caller in this space, and when

        ``GET /insights/background-work``
        """
        return self._c.request("GET", "insights/background-work", params=params)

    def list_tokens_saved(self, **params: Any) -> Any:
        """Tokens saved by AI search, graph search and Ask AI, as running totals

        ``GET /insights/tokens-saved``
        """
        return self._c.request("GET", "insights/tokens-saved", params=params)


class KnowledgeOps(_Namespace):
    """8 operations."""

    def list_index(self, **params: Any) -> Any:
        """The index state of everything you own

        ``GET /knowledge/index``
        """
        return self._c.request("GET", "knowledge/index", params=params)

    def list_history(self, **params: Any) -> Any:
        """What happened to the index, and when

        ``GET /knowledge/index/history``
        """
        return self._c.request("GET", "knowledge/index/history", params=params)

    def create_release(self, *, json: Any = None, **params: Any) -> Any:
        """Index this file (start files held for their owner)

        ``POST /knowledge/index/release``
        """
        return self._c.request("POST", "knowledge/index/release", json=json, params=params)

    def list_summary(self, **params: Any) -> Any:
        """Is everything indexed, and what changed since it was

        ``GET /knowledge/index/summary``
        """
        return self._c.request("GET", "knowledge/index/summary", params=params)

    def get_index(self, entity_type: str, entity_id: str, **params: Any) -> Any:
        """The index state of one thing

        ``GET /knowledge/index/{entity_type}/{entity_id}``
        """
        return self._c.request("GET", f"knowledge/index/{entity_type}/{entity_id}", params=params)

    def reindex_index(self, entity_type: str, entity_id: str, *, json: Any = None, **params: Any) -> Any:
        """Index this again, now

        ``POST /knowledge/index/{entity_type}/{entity_id}/reindex``
        """
        return self._c.request("POST", f"knowledge/index/{entity_type}/{entity_id}/reindex", json=json, params=params)

    def list_search(self, **params: Any) -> Any:
        """Search everything, by name, description and tag

        ``GET /knowledge/search``
        """
        return self._c.request("GET", "knowledge/search", params=params)

    def list_agent(self, **params: Any) -> Any:
        """Search one space for an agent, by words, graph and (optionally) meaning

        ``GET /search/agent``
        """
        return self._c.request("GET", "search/agent", params=params)


class MailOps(_Namespace):
    """52 operations."""

    def list_bulk_sends(self, **params: Any) -> Any:
        """List bulk sends

        ``GET /mail/bulk-sends``
        """
        return self._c.request("GET", "mail/bulk-sends", params=params)

    def create_bulk_sends(self, *, json: Any = None, **params: Any) -> Any:
        """Plan a bulk send

        ``POST /mail/bulk-sends``
        """
        return self._c.request("POST", "mail/bulk-sends", json=json, params=params)

    def get_bulk_sends(self, run_id: str, **params: Any) -> Any:
        """Read a bulk send and its record

        ``GET /mail/bulk-sends/{run_id}``
        """
        return self._c.request("GET", f"mail/bulk-sends/{run_id}", params=params)

    def cancel_bulk_sends(self, run_id: str, *, json: Any = None, **params: Any) -> Any:
        """Cancel a planned bulk send, or undo a held one

        ``POST /mail/bulk-sends/{run_id}/cancel``
        """
        return self._c.request("POST", f"mail/bulk-sends/{run_id}/cancel", json=json, params=params)

    def send_bulk_sends(self, run_id: str, *, json: Any = None, **params: Any) -> Any:
        """Send a planned bulk send

        ``POST /mail/bulk-sends/{run_id}/send``
        """
        return self._c.request("POST", f"mail/bulk-sends/{run_id}/send", json=json, params=params)

    def delete_drafts(self, draft_id: str, **params: Any) -> Any:
        """Discard a draft

        ``DELETE /mail/drafts/{draft_id}``
        """
        return self._c.request("DELETE", f"mail/drafts/{draft_id}", params=params)

    def get_drafts(self, draft_id: str, **params: Any) -> Any:
        """Read one exact draft

        ``GET /mail/drafts/{draft_id}``
        """
        return self._c.request("GET", f"mail/drafts/{draft_id}", params=params)

    def update_drafts(self, draft_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change a draft

        ``PATCH /mail/drafts/{draft_id}``
        """
        return self._c.request("PATCH", f"mail/drafts/{draft_id}", json=json, params=params)

    def attachments_drafts(self, draft_id: str, *, json: Any = None, **params: Any) -> Any:
        """Attach a file to a draft

        ``POST /mail/drafts/{draft_id}/attachments``
        """
        return self._c.request("POST", f"mail/drafts/{draft_id}/attachments", json=json, params=params)

    def delete_attachments(self, draft_id: str, attachment_id: str, **params: Any) -> Any:
        """Take an attachment off a draft

        ``DELETE /mail/drafts/{draft_id}/attachments/{attachment_id}``
        """
        return self._c.request("DELETE", f"mail/drafts/{draft_id}/attachments/{attachment_id}", params=params)

    def send_drafts(self, draft_id: str, *, json: Any = None, **params: Any) -> Any:
        """Send a draft

        ``POST /mail/drafts/{draft_id}/send``
        """
        return self._c.request("POST", f"mail/drafts/{draft_id}/send", json=json, params=params)

    def list_links(self, **params: Any) -> Any:
        """INVRSYS Mail's policy links

        ``GET /mail/links``
        """
        return self._c.request("GET", "mail/links", params=params)

    def list_mailboxes(self, **params: Any) -> Any:
        """Every mailbox you may use

        ``GET /mail/mailboxes``
        """
        return self._c.request("GET", "mail/mailboxes", params=params)

    def update_mailboxes(self, mailbox_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename a mailbox

        ``PATCH /mail/mailboxes/{mailbox_id}``
        """
        return self._c.request("PATCH", f"mail/mailboxes/{mailbox_id}", json=json, params=params)

    def actions_mailboxes(self, mailbox_id: str, *, json: Any = None, **params: Any) -> Any:
        """One action on threads and messages

        ``POST /mail/mailboxes/{mailbox_id}/actions``
        """
        return self._c.request("POST", f"mail/mailboxes/{mailbox_id}/actions", json=json, params=params)

    def get_drafts_mailboxes(self, mailbox_id: str, **params: Any) -> Any:
        """A mailbox's drafts

        ``GET /mail/mailboxes/{mailbox_id}/drafts``
        """
        return self._c.request("GET", f"mail/mailboxes/{mailbox_id}/drafts", params=params)

    def drafts_mailboxes(self, mailbox_id: str, *, json: Any = None, **params: Any) -> Any:
        """A new draft

        ``POST /mail/mailboxes/{mailbox_id}/drafts``
        """
        return self._c.request("POST", f"mail/mailboxes/{mailbox_id}/drafts", json=json, params=params)

    def get_folders_mailboxes(self, mailbox_id: str, **params: Any) -> Any:
        """A mailbox's folders, then its labels

        ``GET /mail/mailboxes/{mailbox_id}/folders``
        """
        return self._c.request("GET", f"mail/mailboxes/{mailbox_id}/folders", params=params)

    def labels_mailboxes(self, mailbox_id: str, *, json: Any = None, **params: Any) -> Any:
        """A new label

        ``POST /mail/mailboxes/{mailbox_id}/labels``
        """
        return self._c.request("POST", f"mail/mailboxes/{mailbox_id}/labels", json=json, params=params)

    def delete_labels(self, mailbox_id: str, label_id: str, **params: Any) -> Any:
        """Remove a label

        ``DELETE /mail/mailboxes/{mailbox_id}/labels/{label_id}``
        """
        return self._c.request("DELETE", f"mail/mailboxes/{mailbox_id}/labels/{label_id}", params=params)

    def update_labels(self, mailbox_id: str, label_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename or recolour a label

        ``PATCH /mail/mailboxes/{mailbox_id}/labels/{label_id}``
        """
        return self._c.request("PATCH", f"mail/mailboxes/{mailbox_id}/labels/{label_id}", json=json, params=params)

    def get_my_settings_mailboxes(self, mailbox_id: str, **params: Any) -> Any:
        """Your own settings for a mailbox

        ``GET /mail/mailboxes/{mailbox_id}/my-settings``
        """
        return self._c.request("GET", f"mail/mailboxes/{mailbox_id}/my-settings", params=params)

    def update_my_settings_mailboxes(self, mailbox_id: str, *, json: Any = None, **params: Any) -> Any:
        """Mute or unmute a mailbox for yourself

        ``PATCH /mail/mailboxes/{mailbox_id}/my-settings``
        """
        return self._c.request("PATCH", f"mail/mailboxes/{mailbox_id}/my-settings", json=json, params=params)

    def get_rules_mailboxes(self, mailbox_id: str, **params: Any) -> Any:
        """A mailbox's rules, in order

        ``GET /mail/mailboxes/{mailbox_id}/rules``
        """
        return self._c.request("GET", f"mail/mailboxes/{mailbox_id}/rules", params=params)

    def rules_mailboxes(self, mailbox_id: str, *, json: Any = None, **params: Any) -> Any:
        """A new rule

        ``POST /mail/mailboxes/{mailbox_id}/rules``
        """
        return self._c.request("POST", f"mail/mailboxes/{mailbox_id}/rules", json=json, params=params)

    def update_order_rules(self, mailbox_id: str, *, json: Any = None, **params: Any) -> Any:
        """Put the rules in order

        ``PUT /mail/mailboxes/{mailbox_id}/rules/order``
        """
        return self._c.request("PUT", f"mail/mailboxes/{mailbox_id}/rules/order", json=json, params=params)

    def test_rules(self, mailbox_id: str, *, json: Any = None, **params: Any) -> Any:
        """Try a rule without saving it

        ``POST /mail/mailboxes/{mailbox_id}/rules/test``
        """
        return self._c.request("POST", f"mail/mailboxes/{mailbox_id}/rules/test", json=json, params=params)

    def delete_rules(self, mailbox_id: str, rule_id: str, **params: Any) -> Any:
        """Delete a rule

        ``DELETE /mail/mailboxes/{mailbox_id}/rules/{rule_id}``
        """
        return self._c.request("DELETE", f"mail/mailboxes/{mailbox_id}/rules/{rule_id}", params=params)

    def get_rules(self, mailbox_id: str, rule_id: str, **params: Any) -> Any:
        """One rule

        ``GET /mail/mailboxes/{mailbox_id}/rules/{rule_id}``
        """
        return self._c.request("GET", f"mail/mailboxes/{mailbox_id}/rules/{rule_id}", params=params)

    def update_rules(self, mailbox_id: str, rule_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change a rule

        ``PATCH /mail/mailboxes/{mailbox_id}/rules/{rule_id}``
        """
        return self._c.request("PATCH", f"mail/mailboxes/{mailbox_id}/rules/{rule_id}", json=json, params=params)

    def get_signatures_mailboxes(self, mailbox_id: str, **params: Any) -> Any:
        """A mailbox's signatures

        ``GET /mail/mailboxes/{mailbox_id}/signatures``
        """
        return self._c.request("GET", f"mail/mailboxes/{mailbox_id}/signatures", params=params)

    def signatures_mailboxes(self, mailbox_id: str, *, json: Any = None, **params: Any) -> Any:
        """A new signature

        ``POST /mail/mailboxes/{mailbox_id}/signatures``
        """
        return self._c.request("POST", f"mail/mailboxes/{mailbox_id}/signatures", json=json, params=params)

    def delete_signatures(self, mailbox_id: str, signature_id: str, **params: Any) -> Any:
        """Remove a signature

        ``DELETE /mail/mailboxes/{mailbox_id}/signatures/{signature_id}``
        """
        return self._c.request("DELETE", f"mail/mailboxes/{mailbox_id}/signatures/{signature_id}", params=params)

    def update_signatures(self, mailbox_id: str, signature_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change a signature

        ``PATCH /mail/mailboxes/{mailbox_id}/signatures/{signature_id}``
        """
        return self._c.request(
            "PATCH", f"mail/mailboxes/{mailbox_id}/signatures/{signature_id}", json=json, params=params
        )

    def get_threads_mailboxes(self, mailbox_id: str, **params: Any) -> Any:
        """A page of threads

        ``GET /mail/mailboxes/{mailbox_id}/threads``
        """
        return self._c.request("GET", f"mail/mailboxes/{mailbox_id}/threads", params=params)

    def get_messages(self, message_id: str, **params: Any) -> Any:
        """One message

        ``GET /mail/messages/{message_id}``
        """
        return self._c.request("GET", f"mail/messages/{message_id}", params=params)

    def get_raw_attachments(self, message_id: str, attachment_id: str, **params: Any) -> Any:
        """Download an attachment from a mailbox you may read

        ``GET /mail/messages/{message_id}/attachments/{attachment_id}/raw``
        """
        return self._c.request("GET", f"mail/messages/{message_id}/attachments/{attachment_id}/raw", params=params)

    def save_attachments(self, message_id: str, attachment_id: str, *, json: Any = None, **params: Any) -> Any:
        """Save an attachment to Drive

        ``POST /mail/messages/{message_id}/attachments/{attachment_id}/save``
        """
        return self._c.request(
            "POST", f"mail/messages/{message_id}/attachments/{attachment_id}/save", json=json, params=params
        )

    def get_delivery_messages(self, message_id: str, **params: Any) -> Any:
        """Who a sent email reached

        ``GET /mail/messages/{message_id}/delivery``
        """
        return self._c.request("GET", f"mail/messages/{message_id}/delivery", params=params)

    def save_messages(self, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Save a whole email to Drive

        ``POST /mail/messages/{message_id}/save``
        """
        return self._c.request("POST", f"mail/messages/{message_id}/save", json=json, params=params)

    def undo_send_messages(self, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Undo a send

        ``POST /mail/messages/{message_id}/undo-send``
        """
        return self._c.request("POST", f"mail/messages/{message_id}/undo-send", json=json, params=params)

    def list_opt_outs(self, **params: Any) -> Any:
        """List who asked not to be mailed

        ``GET /mail/opt-outs``
        """
        return self._c.request("GET", "mail/opt-outs", params=params)

    def create_opt_outs(self, *, json: Any = None, **params: Any) -> Any:
        """Add someone to the opt-out list

        ``POST /mail/opt-outs``
        """
        return self._c.request("POST", "mail/opt-outs", json=json, params=params)

    def delete_opt_outs(self, opt_out_id: str, **params: Any) -> Any:
        """Remove someone from the opt-out list

        ``DELETE /mail/opt-outs/{opt_out_id}``
        """
        return self._c.request("DELETE", f"mail/opt-outs/{opt_out_id}", params=params)

    def list_pictures(self, **params: Any) -> Any:
        """A message's picture from another site, fetched for you

        ``GET /mail/pictures``
        """
        return self._c.request("GET", "mail/pictures", params=params)

    def create_senders(self, *, json: Any = None, **params: Any) -> Any:
        """Put a sender in Focused or Other

        ``POST /mail/senders``
        """
        return self._c.request("POST", "mail/senders", json=json, params=params)

    def list_settings(self, **params: Any) -> Any:
        """Mail's settings

        ``GET /mail/settings``
        """
        return self._c.request("GET", "mail/settings", params=params)

    def update_settings(self, *, json: Any = None, **params: Any) -> Any:
        """Change Mail's settings

        ``PATCH /mail/settings``
        """
        return self._c.request("PATCH", "mail/settings", json=json, params=params)

    def get_threads(self, thread_id: str, **params: Any) -> Any:
        """One conversation with its messages

        ``GET /mail/threads/{thread_id}``
        """
        return self._c.request("GET", f"mail/threads/{thread_id}", params=params)

    def invite_threads(self, thread_id: str, *, json: Any = None, **params: Any) -> Any:
        """Answer a calendar invitation

        ``POST /mail/threads/{thread_id}/invite``
        """
        return self._c.request("POST", f"mail/threads/{thread_id}/invite", json=json, params=params)

    def get_unsubscribe(self, token: str, **params: Any) -> Any:
        """What a bulk mail's unsubscribe link leaves

        ``GET /mail/unsubscribe/{token}``
        """
        return self._c.request("GET", f"mail/unsubscribe/{token}", params=params)

    def create_unsubscribe(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Leave a sender's bulk mail

        ``POST /mail/unsubscribe/{token}``
        """
        return self._c.request("POST", f"mail/unsubscribe/{token}", json=json, params=params)


class MarketOps(_Namespace):
    """14 operations."""

    def list_files(self, **params: Any) -> Any:
        """Browse published files (the Discover tab)

        ``GET /market/files``
        """
        return self._c.request("GET", "market/files", params=params)

    def get_preview_files(self, file_id: str, **params: Any) -> Any:
        """Preview a published file (a teaser, never the file)

        ``GET /market/files/{file_id}/preview``
        """
        return self._c.request("GET", f"market/files/{file_id}/preview", params=params)

    def get_image_preview(self, file_id: str, **params: Any) -> Any:
        """A published image's reduced copy, as a JPEG

        ``GET /market/files/{file_id}/preview/image``
        """
        return self._c.request("GET", f"market/files/{file_id}/preview/image", params=params)

    def get_pages(self, file_id: str, number: str, **params: Any) -> Any:
        """One page of a published PDF's or office file's teaser

        ``GET /market/files/{file_id}/preview/pages/{number}``
        """
        return self._c.request("GET", f"market/files/{file_id}/preview/pages/{number}", params=params)

    def get_poster_preview(self, file_id: str, **params: Any) -> Any:
        """A published video's poster frame, as a JPEG

        ``GET /market/files/{file_id}/preview/poster``
        """
        return self._c.request("GET", f"market/files/{file_id}/preview/poster", params=params)

    def report_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Report something on the shelf

        ``POST /market/files/{file_id}/report``
        """
        return self._c.request("POST", f"market/files/{file_id}/report", json=json, params=params)

    def view_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Record that somebody opened this card

        ``POST /market/files/{file_id}/view``
        """
        return self._c.request("POST", f"market/files/{file_id}/view", json=json, params=params)

    def list_templates(self, **params: Any) -> Any:
        """Browse templates

        ``GET /market/templates``
        """
        return self._c.request("GET", "market/templates", params=params)

    def get_preview_templates(self, template_id: str, **params: Any) -> Any:
        """Preview a template in full, read-only

        ``GET /market/templates/{template_id}/preview``
        """
        return self._c.request("GET", f"market/templates/{template_id}/preview", params=params)

    def get_images(self, template_id: str, key: str, **params: Any) -> Any:
        """One of a built-in template's own pictures, as a JPEG

        ``GET /market/templates/{template_id}/preview/images/{key}``
        """
        return self._c.request("GET", f"market/templates/{template_id}/preview/images/{key}", params=params)

    def delete_rating_templates(self, template_id: str, **params: Any) -> Any:
        """Withdraw your rating

        ``DELETE /market/templates/{template_id}/rating``
        """
        return self._c.request("DELETE", f"market/templates/{template_id}/rating", params=params)

    def update_rating_templates(self, template_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rate a template out of five

        ``PUT /market/templates/{template_id}/rating``
        """
        return self._c.request("PUT", f"market/templates/{template_id}/rating", json=json, params=params)

    def report_templates(self, template_id: str, *, json: Any = None, **params: Any) -> Any:
        """Report a template

        ``POST /market/templates/{template_id}/report``
        """
        return self._c.request("POST", f"market/templates/{template_id}/report", json=json, params=params)

    def view_templates(self, template_id: str, *, json: Any = None, **params: Any) -> Any:
        """Record that a template card was opened

        ``POST /market/templates/{template_id}/view``
        """
        return self._c.request("POST", f"market/templates/{template_id}/view", json=json, params=params)


class NotificationsOps(_Namespace):
    """4 operations."""

    def list_notifications(self, **params: Any) -> Any:
        """List notifications + unread count

        ``GET /notifications/``
        """
        return self._c.request("GET", "notifications/", params=params)

    def create_read_all(self, *, json: Any = None, **params: Any) -> Any:
        """Mark all read

        ``POST /notifications/read-all``
        """
        return self._c.request("POST", "notifications/read-all", json=json, params=params)

    def read_notifications(self, notification_id: str, *, json: Any = None, **params: Any) -> Any:
        """Mark one notification read

        ``POST /notifications/{notification_id}/read``
        """
        return self._c.request("POST", f"notifications/{notification_id}/read", json=json, params=params)

    def unread_notifications(self, notification_id: str, *, json: Any = None, **params: Any) -> Any:
        """Mark a notification unread again

        ``POST /notifications/{notification_id}/unread``
        """
        return self._c.request("POST", f"notifications/{notification_id}/unread", json=json, params=params)


class OpsOps(_Namespace):
    """1 operations."""

    def list_health(self, **params: Any) -> Any:
        """Liveness/readiness (note - served at /health/, outside /api/v1)

        ``GET /health/``
        """
        return self._c.request("GET", "health/", params=params)


class PublicOps(_Namespace):
    """36 operations."""

    def list_embed_js(self, **params: Any) -> Any:
        """The loader a site pastes beside its embed

        ``GET /embed.js``
        """
        return self._c.request("GET", "embed.js", params=params)

    def list_entries(self, **params: Any) -> Any:
        """The help centre's published entries, or a search of them

        ``GET /help/entries``
        """
        return self._c.request("GET", "help/entries", params=params)

    def get_entries(self, slug: str, **params: Any) -> Any:
        """One published help entry, its body as read

        ``GET /help/entries/{slug}``
        """
        return self._c.request("GET", f"help/entries/{slug}", params=params)

    def create_abuse_reports(self, *, json: Any = None, **params: Any) -> Any:
        """Report published content

        ``POST /public/abuse-reports``
        """
        return self._c.request("POST", "public/abuse-reports", json=json, params=params)

    def list_api(self, **params: Any) -> Any:
        """The REST catalogue, or the OpenAPI document itself

        ``GET /public/api``
        """
        return self._c.request("GET", "public/api", params=params)

    def get_cancel(self, cancel_token: str, **params: Any) -> Any:
        """The booking a cancel token points at

        ``GET /public/booking/cancel/{cancel_token}``
        """
        return self._c.request("GET", f"public/booking/cancel/{cancel_token}", params=params)

    def create_cancel(self, cancel_token: str, *, json: Any = None, **params: Any) -> Any:
        """Cancel a booking with its token

        ``POST /public/booking/cancel/{cancel_token}``
        """
        return self._c.request("POST", f"public/booking/cancel/{cancel_token}", json=json, params=params)

    def get_invite(self, token: str, **params: Any) -> Any:
        """The meeting as a calendar file

        ``GET /public/booking/invite/{token}.ics``
        """
        return self._c.request("GET", f"public/booking/invite/{token}.ics", params=params)

    def get_booking(self, slug: str, **params: Any) -> Any:
        """A booking page, as a visitor sees it

        ``GET /public/booking/{slug}``
        """
        return self._c.request("GET", f"public/booking/{slug}", params=params)

    def book_booking(self, slug: str, *, json: Any = None, **params: Any) -> Any:
        """Book a slot

        ``POST /public/booking/{slug}/book``
        """
        return self._c.request("POST", f"public/booking/{slug}/book", json=json, params=params)

    def get_slots_booking(self, slug: str, **params: Any) -> Any:
        """The slots a visitor can pick

        ``GET /public/booking/{slug}/slots``
        """
        return self._c.request("GET", f"public/booking/{slug}/slots", params=params)

    def verify_booking(self, slug: str, *, json: Any = None, **params: Any) -> Any:
        """Ask for a one-time code

        ``POST /public/booking/{slug}/verify``
        """
        return self._c.request("POST", f"public/booking/{slug}/verify", json=json, params=params)

    def confirm_verify(self, slug: str, *, json: Any = None, **params: Any) -> Any:
        """Spend a code for a booking window

        ``POST /public/booking/{slug}/verify/confirm``
        """
        return self._c.request("POST", f"public/booking/{slug}/verify/confirm", json=json, params=params)

    def get_invites(self, token: str, **params: Any) -> Any:
        """An event invitation, from its email

        ``GET /public/calendar/invites/{token}``
        """
        return self._c.request("GET", f"public/calendar/invites/{token}", params=params)

    def create_invites(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Answer an event invitation, from its email

        ``POST /public/calendar/invites/{token}``
        """
        return self._c.request("POST", f"public/calendar/invites/{token}", json=json, params=params)

    def get_calendar_invites(self, token: str, **params: Any) -> Any:
        """An event invitation as a calendar file

        ``GET /public/calendar/invites/{token}.ics``
        """
        return self._c.request("GET", f"public/calendar/invites/{token}.ics", params=params)

    def forward_invites(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Forward an event invitation, from its email

        ``POST /public/calendar/invites/{token}/forward``
        """
        return self._c.request("POST", f"public/calendar/invites/{token}/forward", json=json, params=params)

    def get_meet_card(self, token: str, **params: Any) -> Any:
        """The card image a meeting guest link shows when pasted

        ``GET /public/calendar/meet-card/{token}.png``
        """
        return self._c.request("GET", f"public/calendar/meet-card/{token}.png", params=params)

    def get_canvas(self, slug: str, **params: Any) -> Any:
        """Read a published board

        ``GET /public/canvas/{slug}``
        """
        return self._c.request("GET", f"public/canvas/{slug}", params=params)

    def get_forms(self, slug: str, **params: Any) -> Any:
        """A form, as a visitor sees it

        ``GET /public/forms/{slug}``
        """
        return self._c.request("GET", f"public/forms/{slug}", params=params)

    def files_forms(self, slug: str, *, json: Any = None, **params: Any) -> Any:
        """Upload a file for a file or signature question

        ``POST /public/forms/{slug}/files``
        """
        return self._c.request("POST", f"public/forms/{slug}/files", json=json, params=params)

    def responses_forms(self, slug: str, *, json: Any = None, **params: Any) -> Any:
        """Answer a form

        ``POST /public/forms/{slug}/responses``
        """
        return self._c.request("POST", f"public/forms/{slug}/responses", json=json, params=params)

    def list_legal(self, **params: Any) -> Any:
        """The terms and privacy documents to link at signup

        ``GET /public/legal``
        """
        return self._c.request("GET", "public/legal", params=params)

    def list_mcp(self, **params: Any) -> Any:
        """The MCP tool catalogue

        ``GET /public/mcp``
        """
        return self._c.request("GET", "public/mcp", params=params)

    def get_media(self, file_id: str, **params: Any) -> Any:
        """An image embedded in published content

        ``GET /public/media/{file_id}``
        """
        return self._c.request("GET", f"public/media/{file_id}", params=params)

    def get_renditions(self, file_id: str, size: str, **params: Any) -> Any:
        """A published gallery image's resized copy

        ``GET /public/media/{file_id}/renditions/{size}``
        """
        return self._c.request("GET", f"public/media/{file_id}/renditions/{size}", params=params)

    def get_notes(self, slug: str, **params: Any) -> Any:
        """Read a published note

        ``GET /public/notes/{slug}``
        """
        return self._c.request("GET", f"public/notes/{slug}", params=params)

    def get_pages(self, slug: str, path: str, **params: Any) -> Any:
        """One page inside a published site

        ``GET /public/pages/{slug}/{path}``
        """
        return self._c.request("GET", f"public/pages/{slug}/{path}", params=params)

    def list_plans(self, **params: Any) -> Any:
        """The plans the marketing site lists

        ``GET /public/plans``
        """
        return self._c.request("GET", "public/plans", params=params)

    def get_embed(self, code: str, **params: Any) -> Any:
        """What an embed is showing, for a client that did not get our HTML

        ``GET /public/reach/embed/{code}``
        """
        return self._c.request("GET", f"public/reach/embed/{code}", params=params)

    def get_files(self, token: str, file_id: str, **params: Any) -> Any:
        """Download one file from a shared folder

        ``GET /public/share/{token}/files/{file_id}``
        """
        return self._c.request("GET", f"public/share/{token}/files/{file_id}", params=params)

    def get_zip_share(self, token: str, **params: Any) -> Any:
        """Download a shared folder as a zip

        ``GET /public/share/{token}/zip``
        """
        return self._c.request("GET", f"public/share/{token}/zip", params=params)

    def get_sites(self, slug: str, **params: Any) -> Any:
        """A published site's home page and its nav

        ``GET /public/sites/{slug}``
        """
        return self._c.request("GET", f"public/sites/{slug}", params=params)

    def get_frame_sites(self, slug: str, **params: Any) -> Any:
        """What frames every page of a published site

        ``GET /public/sites/{slug}/frame``
        """
        return self._c.request("GET", f"public/sites/{slug}/frame", params=params)

    def get_by_id(self, table_id: str, **params: Any) -> Any:
        """A published table by id, for a card embedded elsewhere

        ``GET /public/tables/by-id/{table_id}``
        """
        return self._c.request("GET", f"public/tables/by-id/{table_id}", params=params)

    def get_tables(self, slug: str, **params: Any) -> Any:
        """Read a published table

        ``GET /public/tables/{slug}``
        """
        return self._c.request("GET", f"public/tables/{slug}", params=params)


class PublishingOps(_Namespace):
    """12 operations."""

    def get_publish_canvas(self, canvas_id: str, **params: Any) -> Any:
        """Is this board published, and where

        ``GET /canvas/{canvas_id}/publish``
        """
        return self._c.request("GET", f"canvas/{canvas_id}/publish", params=params)

    def publish_canvas(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Publish or unpublish a board

        ``POST /canvas/{canvas_id}/publish``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/publish", json=json, params=params)

    def list_sites(self, **params: Any) -> Any:
        """List your published sites

        ``GET /publishing/sites``
        """
        return self._c.request("GET", "publishing/sites", params=params)

    def delete_sites(self, site_id: str, **params: Any) -> Any:
        """Take a whole site down

        ``DELETE /publishing/sites/{site_id}``
        """
        return self._c.request("DELETE", f"publishing/sites/{site_id}", params=params)

    def update_sites(self, site_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change a site's description, look, address or home

        ``PATCH /publishing/sites/{site_id}``
        """
        return self._c.request("PATCH", f"publishing/sites/{site_id}", json=json, params=params)

    def update_pages(self, site_id: str, page_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename or reorder a page within a site

        ``PATCH /publishing/sites/{site_id}/pages/{page_id}``
        """
        return self._c.request("PATCH", f"publishing/sites/{site_id}/pages/{page_id}", json=json, params=params)

    def get_publish_files(self, file_id: str, **params: Any) -> Any:
        """Is this note published, and at what URL

        ``GET /storage/files/{file_id}/publish``
        """
        return self._c.request("GET", f"storage/files/{file_id}/publish", params=params)

    def publish_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Publish or unpublish a note

        ``POST /storage/files/{file_id}/publish``
        """
        return self._c.request("POST", f"storage/files/{file_id}/publish", json=json, params=params)

    def get_publish_folders(self, folder_id: str, **params: Any) -> Any:
        """Is this folder published as a gallery

        ``GET /storage/folders/{folder_id}/publish``
        """
        return self._c.request("GET", f"storage/folders/{folder_id}/publish", params=params)

    def publish_folders(self, folder_id: str, *, json: Any = None, **params: Any) -> Any:
        """Publish a folder as a public gallery

        ``POST /storage/folders/{folder_id}/publish``
        """
        return self._c.request("POST", f"storage/folders/{folder_id}/publish", json=json, params=params)

    def get_publish_tables(self, table_id: str, **params: Any) -> Any:
        """Is this table published, and where

        ``GET /tables/{table_id}/publish``
        """
        return self._c.request("GET", f"tables/{table_id}/publish", params=params)

    def publish_tables(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Publish or unpublish a table

        ``POST /tables/{table_id}/publish``
        """
        return self._c.request("POST", f"tables/{table_id}/publish", json=json, params=params)


class RagOps(_Namespace):
    """46 operations."""

    def create_actions(self, *, json: Any = None, **params: Any) -> Any:
        """Run an AI action on a piece of text

        ``POST /rag/actions``
        """
        return self._c.request("POST", "rag/actions", json=json, params=params)

    def list_capability(self, **params: Any) -> Any:
        """Is semantic search and chat available at all

        ``GET /rag/capability``
        """
        return self._c.request("GET", "rag/capability", params=params)

    def get_made(self, entity_id: str, **params: Any) -> Any:
        """Which of your conversations made this file

        ``GET /rag/chat/made/{entity_id}``
        """
        return self._c.request("GET", f"rag/chat/made/{entity_id}", params=params)

    def list_sessions(self, **params: Any) -> Any:
        """List chat sessions

        ``GET /rag/chat/sessions``
        """
        return self._c.request("GET", "rag/chat/sessions", params=params)

    def create_sessions(self, *, json: Any = None, **params: Any) -> Any:
        """Start a chat session

        ``POST /rag/chat/sessions``
        """
        return self._c.request("POST", "rag/chat/sessions", json=json, params=params)

    def delete_sessions(self, session_id: str, **params: Any) -> Any:
        """Delete a session

        ``DELETE /rag/chat/sessions/{session_id}``
        """
        return self._c.request("DELETE", f"rag/chat/sessions/{session_id}", params=params)

    def get_sessions(self, session_id: str, **params: Any) -> Any:
        """Read a session and its messages

        ``GET /rag/chat/sessions/{session_id}``
        """
        return self._c.request("GET", f"rag/chat/sessions/{session_id}", params=params)

    def update_sessions(self, session_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename, pin, set memory, or point a session's uploads somewhere

        ``PATCH /rag/chat/sessions/{session_id}``
        """
        return self._c.request("PATCH", f"rag/chat/sessions/{session_id}", json=json, params=params)

    def compact_sessions(self, session_id: str, *, json: Any = None, **params: Any) -> Any:
        """Compact this conversation (`/compact`)

        ``POST /rag/chat/sessions/{session_id}/compact``
        """
        return self._c.request("POST", f"rag/chat/sessions/{session_id}/compact", json=json, params=params)

    def get_files_sessions(self, session_id: str, **params: Any) -> Any:
        """The files Flowpy made in this conversation

        ``GET /rag/chat/sessions/{session_id}/files``
        """
        return self._c.request("GET", f"rag/chat/sessions/{session_id}/files", params=params)

    def delete_files(self, session_id: str, draft_id: str, **params: Any) -> Any:
        """Discard a file Flowpy made, before it was saved

        ``DELETE /rag/chat/sessions/{session_id}/files/{draft_id}``
        """
        return self._c.request("DELETE", f"rag/chat/sessions/{session_id}/files/{draft_id}", params=params)

    def get_files(self, session_id: str, draft_id: str, **params: Any) -> Any:
        """One file Flowpy made, whole

        ``GET /rag/chat/sessions/{session_id}/files/{draft_id}``
        """
        return self._c.request("GET", f"rag/chat/sessions/{session_id}/files/{draft_id}", params=params)

    def get_download_files(self, session_id: str, draft_id: str, **params: Any) -> Any:
        """Download a file Flowpy made

        ``GET /rag/chat/sessions/{session_id}/files/{draft_id}/download``
        """
        return self._c.request("GET", f"rag/chat/sessions/{session_id}/files/{draft_id}/download", params=params)

    def save_files(self, session_id: str, draft_id: str, *, json: Any = None, **params: Any) -> Any:
        """Save a file Flowpy made into Drive

        ``POST /rag/chat/sessions/{session_id}/files/{draft_id}/save``
        """
        return self._c.request(
            "POST", f"rag/chat/sessions/{session_id}/files/{draft_id}/save", json=json, params=params
        )

    def messages_sessions(self, session_id: str, *, json: Any = None, **params: Any) -> Any:
        """Ask a question in a session

        ``POST /rag/chat/sessions/{session_id}/messages``
        """
        return self._c.request("POST", f"rag/chat/sessions/{session_id}/messages", json=json, params=params)

    def create_confirm(self, session_id: str, message_id: str, card_id: str, *, json: Any = None, **params: Any) -> Any:
        """Confirm or cancel a change Flowpy proposed

        ``POST /rag/chat/sessions/{session_id}/messages/{message_id}/confirm/{card_id}``
        """
        return self._c.request(
            "POST", f"rag/chat/sessions/{session_id}/messages/{message_id}/confirm/{card_id}", json=json, params=params
        )

    def draft_states_messages(self, session_id: str, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Where this answer's draft cards stand

        ``POST /rag/chat/sessions/{session_id}/messages/{message_id}/draft-states``
        """
        return self._c.request(
            "POST", f"rag/chat/sessions/{session_id}/messages/{message_id}/draft-states", json=json, params=params
        )

    def select_messages(self, session_id: str, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Show this version of an answer

        ``POST /rag/chat/sessions/{session_id}/messages/{message_id}/select``
        """
        return self._c.request(
            "POST", f"rag/chat/sessions/{session_id}/messages/{message_id}/select", json=json, params=params
        )

    def send_again_messages(self, session_id: str, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Send a sent email again to the people it missed

        ``POST /rag/chat/sessions/{session_id}/messages/{message_id}/send-again``
        """
        return self._c.request(
            "POST", f"rag/chat/sessions/{session_id}/messages/{message_id}/send-again", json=json, params=params
        )

    def send_draft_messages(self, session_id: str, message_id: str, *, json: Any = None, **params: Any) -> Any:
        """Ask to send a draft from its card

        ``POST /rag/chat/sessions/{session_id}/messages/{message_id}/send-draft``
        """
        return self._c.request(
            "POST", f"rag/chat/sessions/{session_id}/messages/{message_id}/send-draft", json=json, params=params
        )

    def get_sources(self, session_id: str, message_id: str, entity_id: str, **params: Any) -> Any:
        """One cited source of an answer, for the source panel

        ``GET /rag/chat/sessions/{session_id}/messages/{message_id}/sources/{entity_id}``
        """
        return self._c.request(
            "GET", f"rag/chat/sessions/{session_id}/messages/{message_id}/sources/{entity_id}", params=params
        )

    def delete_waiting_messages(self, session_id: str, message_id: str, **params: Any) -> Any:
        """Cancel the answer waiting for an attached recording

        ``DELETE /rag/chat/sessions/{session_id}/messages/{message_id}/waiting``
        """
        return self._c.request("DELETE", f"rag/chat/sessions/{session_id}/messages/{message_id}/waiting", params=params)

    def get_waiting_messages(self, session_id: str, message_id: str, **params: Any) -> Any:
        """A pending answer's progress while its recording is transcribed

        ``GET /rag/chat/sessions/{session_id}/messages/{message_id}/waiting``
        """
        return self._c.request("GET", f"rag/chat/sessions/{session_id}/messages/{message_id}/waiting", params=params)

    def note_sessions(self, session_id: str, *, json: Any = None, **params: Any) -> Any:
        """Save this conversation as a note

        ``POST /rag/chat/sessions/{session_id}/note``
        """
        return self._c.request("POST", f"rag/chat/sessions/{session_id}/note", json=json, params=params)

    def regenerate_sessions(self, session_id: str, *, json: Any = None, **params: Any) -> Any:
        """Answer the last question again

        ``POST /rag/chat/sessions/{session_id}/regenerate``
        """
        return self._c.request("POST", f"rag/chat/sessions/{session_id}/regenerate", json=json, params=params)

    def upload_folder_sessions(self, session_id: str, *, json: Any = None, **params: Any) -> Any:
        """Where a file attached to this conversation should be uploaded

        ``POST /rag/chat/sessions/{session_id}/upload-folder``
        """
        return self._c.request("POST", f"rag/chat/sessions/{session_id}/upload-folder", json=json, params=params)

    def list_daily_brief(self, **params: Any) -> Any:
        """My day, as Flowpy's Brief me gathers it

        ``GET /rag/flowpy/daily-brief``
        """
        return self._c.request("GET", "rag/flowpy/daily-brief", params=params)

    def create_meeting_prep(self, *, json: Any = None, **params: Any) -> Any:
        """Prepare for a meeting, saved as a note

        ``POST /rag/flowpy/meeting-prep``
        """
        return self._c.request("POST", "rag/flowpy/meeting-prep", json=json, params=params)

    def delete_memories(self, **params: Any) -> Any:
        """Delete all my memories here, or everywhere

        ``DELETE /rag/flowpy/memories``
        """
        return self._c.request("DELETE", "rag/flowpy/memories", params=params)

    def list_memories(self, **params: Any) -> Any:
        """What Flowpy remembers for me here

        ``GET /rag/flowpy/memories``
        """
        return self._c.request("GET", "rag/flowpy/memories", params=params)

    def delete_flowpy_memories(self, memory_id: str, **params: Any) -> Any:
        """Delete one memory

        ``DELETE /rag/flowpy/memories/{memory_id}``
        """
        return self._c.request("DELETE", f"rag/flowpy/memories/{memory_id}", params=params)

    def list_memory(self, **params: Any) -> Any:
        """My Flowpy memory switch

        ``GET /rag/flowpy/memory``
        """
        return self._c.request("GET", "rag/flowpy/memory", params=params)

    def update_memory(self, *, json: Any = None, **params: Any) -> Any:
        """Turn my Flowpy memory on or off

        ``PUT /rag/flowpy/memory``
        """
        return self._c.request("PUT", "rag/flowpy/memory", json=json, params=params)

    def delete_preferences(self, **params: Any) -> Any:
        """Reset my Flowpy preferences

        ``DELETE /rag/flowpy/preferences``
        """
        return self._c.request("DELETE", "rag/flowpy/preferences", params=params)

    def list_preferences(self, **params: Any) -> Any:
        """My Flowpy preferences

        ``GET /rag/flowpy/preferences``
        """
        return self._c.request("GET", "rag/flowpy/preferences", params=params)

    def update_preferences(self, *, json: Any = None, **params: Any) -> Any:
        """Set my Flowpy preferences

        ``PUT /rag/flowpy/preferences``
        """
        return self._c.request("PUT", "rag/flowpy/preferences", json=json, params=params)

    def delete_workspace_rules(self, **params: Any) -> Any:
        """Reset this workspace's rules for Flowpy

        ``DELETE /rag/flowpy/workspace-rules``
        """
        return self._c.request("DELETE", "rag/flowpy/workspace-rules", params=params)

    def list_workspace_rules(self, **params: Any) -> Any:
        """This workspace's rules for Flowpy

        ``GET /rag/flowpy/workspace-rules``
        """
        return self._c.request("GET", "rag/flowpy/workspace-rules", params=params)

    def update_workspace_rules(self, *, json: Any = None, **params: Any) -> Any:
        """Set this workspace's rules for Flowpy

        ``PUT /rag/flowpy/workspace-rules``
        """
        return self._c.request("PUT", "rag/flowpy/workspace-rules", json=json, params=params)

    def list_index(self, **params: Any) -> Any:
        """Freshness and size of your semantic index

        ``GET /rag/index``
        """
        return self._c.request("GET", "rag/index", params=params)

    def create_rebuild(self, *, json: Any = None, **params: Any) -> Any:
        """Re-index what is out of date, or everything

        ``POST /rag/index/rebuild``
        """
        return self._c.request("POST", "rag/index/rebuild", json=json, params=params)

    def create_live_voice_sessions(self, *, json: Any = None, **params: Any) -> Any:
        """Admit one authenticated live transcription session

        ``POST /rag/live-voice/sessions``
        """
        return self._c.request("POST", "rag/live-voice/sessions", json=json, params=params)

    def create_prompt_estimate(self, *, json: Any = None, **params: Any) -> Any:
        """What a message will cost beyond the normal price, before sending

        ``POST /rag/prompt-estimate``
        """
        return self._c.request("POST", "rag/prompt-estimate", json=json, params=params)

    def list_search(self, **params: Any) -> Any:
        """Search by meaning, over document content

        ``GET /rag/search``
        """
        return self._c.request("GET", "rag/search", params=params)

    def get_similar(self, file_id: str, **params: Any) -> Any:
        """Images that LOOK like this one

        ``GET /rag/similar/{file_id}``
        """
        return self._c.request("GET", f"rag/similar/{file_id}", params=params)

    def create_transcribe(self, *, json: Any = None, **params: Any) -> Any:
        """Transcribe audio to text

        ``POST /rag/transcribe``
        """
        return self._c.request("POST", "rag/transcribe", json=json, params=params)


class ReachOps(_Namespace):
    """11 operations."""

    def list_oembed(self, **params: Any) -> Any:
        """oEmbed for a public page of ours (REACH_DISCOVERY S6, round 3)

        ``GET /public/oembed``
        """
        return self._c.request("GET", "public/oembed", params=params)

    def list_links(self, **params: Any) -> Any:
        """Your short links

        ``GET /reach/links``
        """
        return self._c.request("GET", "reach/links", params=params)

    def create_links(self, *, json: Any = None, **params: Any) -> Any:
        """The short link for a thing, made on first ask

        ``POST /reach/links``
        """
        return self._c.request("POST", "reach/links", json=json, params=params)

    def delete_links(self, link_id: str, **params: Any) -> Any:
        """Revoke a short link

        ``DELETE /reach/links/{link_id}``
        """
        return self._c.request("DELETE", f"reach/links/{link_id}", params=params)

    def get_links(self, link_id: str, **params: Any) -> Any:
        """One short link

        ``GET /reach/links/{link_id}``
        """
        return self._c.request("GET", f"reach/links/{link_id}", params=params)

    def update_links(self, link_id: str, *, json: Any = None, **params: Any) -> Any:
        """Alias, expiry, revoke

        ``PATCH /reach/links/{link_id}``
        """
        return self._c.request("PATCH", f"reach/links/{link_id}", json=json, params=params)

    def get_embed_links(self, link_id: str, **params: Any) -> Any:
        """An embed's settings, its snippet, and who may frame it

        ``GET /reach/links/{link_id}/embed``
        """
        return self._c.request("GET", f"reach/links/{link_id}/embed", params=params)

    def update_embed_links(self, link_id: str, *, json: Any = None, **params: Any) -> Any:
        """Who may frame this embed, and whether it is signed

        ``PATCH /reach/links/{link_id}/embed``
        """
        return self._c.request("PATCH", f"reach/links/{link_id}/embed", json=json, params=params)

    def get_qr_png_links(self, link_id: str, **params: Any) -> Any:
        """The QR code as PNG, rendered on demand

        ``GET /reach/links/{link_id}/qr.png``
        """
        return self._c.request("GET", f"reach/links/{link_id}/qr.png", params=params)

    def get_qr_svg_links(self, link_id: str, **params: Any) -> Any:
        """The QR code as SVG, rendered on demand

        ``GET /reach/links/{link_id}/qr.svg``
        """
        return self._c.request("GET", f"reach/links/{link_id}/qr.svg", params=params)

    def get_stats_links(self, link_id: str, **params: Any) -> Any:
        """Opens, people and where they came from

        ``GET /reach/links/{link_id}/stats``
        """
        return self._c.request("GET", f"reach/links/{link_id}/stats", params=params)


class SharingOps(_Namespace):
    """27 operations."""

    def get_permissions_canvas(self, canvas_id: str, **params: Any) -> Any:
        """Who has been given access to this board

        ``GET /canvas/{canvas_id}/permissions``
        """
        return self._c.request("GET", f"canvas/{canvas_id}/permissions", params=params)

    def permissions_canvas(self, canvas_id: str, *, json: Any = None, **params: Any) -> Any:
        """Give a person access to this board

        ``POST /canvas/{canvas_id}/permissions``
        """
        return self._c.request("POST", f"canvas/{canvas_id}/permissions", json=json, params=params)

    def get_share(self, token: str, **params: Any) -> Any:
        """Resolve a public share (no auth)

        ``GET /public/share/{token}``
        """
        return self._c.request("GET", f"public/share/{token}", params=params)

    def create_share(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Unlock a password-protected share

        ``POST /public/share/{token}``
        """
        return self._c.request("POST", f"public/share/{token}", json=json, params=params)

    def get_download_share(self, token: str, **params: Any) -> Any:
        """Download a shared file's bytes (no account)

        ``GET /public/share/{token}/download``
        """
        return self._c.request("GET", f"public/share/{token}/download", params=params)

    def get_pages(self, token: str, number: str, **params: Any) -> Any:
        """One drawn page of a shared office file, as a WebP (no account)

        ``GET /public/share/{token}/pages/{number}``
        """
        return self._c.request("GET", f"public/share/{token}/pages/{number}", params=params)

    def get_preview_share(self, token: str, **params: Any) -> Any:
        """Read a shared Word document (no account)

        ``GET /public/share/{token}/preview``
        """
        return self._c.request("GET", f"public/share/{token}/preview", params=params)

    def get_view_share(self, token: str, **params: Any) -> Any:
        """Read a shared PDF on the share page (no account)

        ``GET /public/share/{token}/view``
        """
        return self._c.request("GET", f"public/share/{token}/view", params=params)

    def get_permissions_files(self, file_id: str, **params: Any) -> Any:
        """Who has been given access to this file

        ``GET /storage/files/{file_id}/permissions``
        """
        return self._c.request("GET", f"storage/files/{file_id}/permissions", params=params)

    def permissions_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Give a person access to this file

        ``POST /storage/files/{file_id}/permissions``
        """
        return self._c.request("POST", f"storage/files/{file_id}/permissions", json=json, params=params)

    def request_edit_access_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Ask for edit access to a file shared with you

        ``POST /storage/files/{file_id}/request-edit-access``
        """
        return self._c.request("POST", f"storage/files/{file_id}/request-edit-access", json=json, params=params)

    def get_share_files(self, file_id: str, **params: Any) -> Any:
        """Read the file's current share link, if any

        ``GET /storage/files/{file_id}/share``
        """
        return self._c.request("GET", f"storage/files/{file_id}/share", params=params)

    def share_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Create a public share link

        ``POST /storage/files/{file_id}/share``
        """
        return self._c.request("POST", f"storage/files/{file_id}/share", json=json, params=params)

    def get_permissions_folders(self, folder_id: str, **params: Any) -> Any:
        """Who has been given access to this folder

        ``GET /storage/folders/{folder_id}/permissions``
        """
        return self._c.request("GET", f"storage/folders/{folder_id}/permissions", params=params)

    def permissions_folders(self, folder_id: str, *, json: Any = None, **params: Any) -> Any:
        """Give a person access to a folder and everything under it

        ``POST /storage/folders/{folder_id}/permissions``
        """
        return self._c.request("POST", f"storage/folders/{folder_id}/permissions", json=json, params=params)

    def get_share_folders(self, folder_id: str, **params: Any) -> Any:
        """Read the folder's current share link, if any

        ``GET /storage/folders/{folder_id}/share``
        """
        return self._c.request("GET", f"storage/folders/{folder_id}/share", params=params)

    def share_folders(self, folder_id: str, *, json: Any = None, **params: Any) -> Any:
        """Create a public link to a folder

        ``POST /storage/folders/{folder_id}/share``
        """
        return self._c.request("POST", f"storage/folders/{folder_id}/share", json=json, params=params)

    def delete_permissions(self, permission_id: str, **params: Any) -> Any:
        """Withdraw one person's access

        ``DELETE /storage/permissions/{permission_id}``
        """
        return self._c.request("DELETE", f"storage/permissions/{permission_id}", params=params)

    def list_shared_by_me(self, **params: Any) -> Any:
        """What you have shared with other people

        ``GET /storage/shared-by-me``
        """
        return self._c.request("GET", "storage/shared-by-me", params=params)

    def list_shared_with_me(self, **params: Any) -> Any:
        """Files, folders, boards and tables other people shared with you

        ``GET /storage/shared-with-me``
        """
        return self._c.request("GET", "storage/shared-with-me", params=params)

    def copy_shared(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Copy a file shared with me, or published, into a workspace of my own

        ``POST /storage/shared/{file_id}/copy``
        """
        return self._c.request("POST", f"storage/shared/{file_id}/copy", json=json, params=params)

    def list_shares(self, **params: Any) -> Any:
        """List my active share links

        ``GET /storage/shares``
        """
        return self._c.request("GET", "storage/shares", params=params)

    def delete_shares(self, share_id: str, **params: Any) -> Any:
        """Revoke a share link

        ``DELETE /storage/shares/{share_id}``
        """
        return self._c.request("DELETE", f"storage/shares/{share_id}", params=params)

    def update_shares(self, share_id: str, *, json: Any = None, **params: Any) -> Any:
        """Edit a live share link

        ``PATCH /storage/shares/{share_id}``
        """
        return self._c.request("PATCH", f"storage/shares/{share_id}", json=json, params=params)

    def get_access_shares(self, share_id: str, **params: Any) -> Any:
        """Who has opened this link, and when

        ``GET /storage/shares/{share_id}/access``
        """
        return self._c.request("GET", f"storage/shares/{share_id}/access", params=params)

    def get_permissions_tables(self, table_id: str, **params: Any) -> Any:
        """Who has been given access to this table

        ``GET /tables/{table_id}/permissions``
        """
        return self._c.request("GET", f"tables/{table_id}/permissions", params=params)

    def permissions_tables(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Give a person access to this table

        ``POST /tables/{table_id}/permissions``
        """
        return self._c.request("POST", f"tables/{table_id}/permissions", json=json, params=params)


class StorageOps(_Namespace):
    """58 operations."""

    def list_home(self, **params: Any) -> Any:
        """Everything the Home screen draws, in one request

        ``GET /home``
        """
        return self._c.request("GET", "home", params=params)

    def list_brief(self, **params: Any) -> Any:
        """The day's brief for Home, written by AI once a day, or by rules

        ``GET /home/brief``
        """
        return self._c.request("GET", "home/brief", params=params)

    def list_layout(self, **params: Any) -> Any:
        """The person's saved Home layout

        ``GET /home/layout``
        """
        return self._c.request("GET", "home/layout", params=params)

    def update_layout(self, *, json: Any = None, **params: Any) -> Any:
        """Save the Home layout

        ``PUT /home/layout``
        """
        return self._c.request("PUT", "home/layout", json=json, params=params)

    def list_pulse(self, **params: Any) -> Any:
        """Items changed per local day in the acting space, and its top collaborators

        ``GET /home/pulse``
        """
        return self._c.request("GET", "home/pulse", params=params)

    def create_batch(self, *, json: Any = None, **params: Any) -> Any:
        """Trash, restore, purge, move or star many items in one call

        ``POST /storage/batch``
        """
        return self._c.request("POST", "storage/batch", json=json, params=params)

    def list_camera_backup(self, **params: Any) -> Any:
        """Get/create the "Camera Backup" folder

        ``GET /storage/camera-backup``
        """
        return self._c.request("GET", "storage/camera-backup", params=params)

    def list_download(self, **params: Any) -> Any:
        """Bulk-download a selection of files and folders as one .zip

        ``GET /storage/download``
        """
        return self._c.request("GET", "storage/download", params=params)

    def list_files(self, **params: Any) -> Any:
        """List files (by folder, or every folder with ?scope=all; excludes trashed)

        ``GET /storage/files``
        """
        return self._c.request("GET", "storage/files", params=params)

    def delete_files(self, file_id: str, **params: Any) -> Any:
        """Soft-delete a file (to trash; still counts to quota)

        ``DELETE /storage/files/{file_id}``
        """
        return self._c.request("DELETE", f"storage/files/{file_id}", params=params)

    def get_files(self, file_id: str, **params: Any) -> Any:
        """One file's metadata by id

        ``GET /storage/files/{file_id}``
        """
        return self._c.request("GET", f"storage/files/{file_id}", params=params)

    def update_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename, move, star, or edit a file's description/tags

        ``PATCH /storage/files/{file_id}``
        """
        return self._c.request("PATCH", f"storage/files/{file_id}", json=json, params=params)

    def get_content_files(self, file_id: str, **params: Any) -> Any:
        """Read a text file's content inline

        ``GET /storage/files/{file_id}/content``
        """
        return self._c.request("GET", f"storage/files/{file_id}/content", params=params)

    def update_content_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Save a text file's content inline

        ``PUT /storage/files/{file_id}/content``
        """
        return self._c.request("PUT", f"storage/files/{file_id}/content", json=json, params=params)

    def copy_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Make a copy of one of my files

        ``POST /storage/files/{file_id}/copy``
        """
        return self._c.request("POST", f"storage/files/{file_id}/copy", json=json, params=params)

    def discoverable_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Toggle discoverability / mature flag (owner only)

        ``POST /storage/files/{file_id}/discoverable``
        """
        return self._c.request("POST", f"storage/files/{file_id}/discoverable", json=json, params=params)

    def get_download_files(self, file_id: str, **params: Any) -> Any:
        """Get a URL to fetch the file's bytes (owner)

        ``GET /storage/files/{file_id}/download``
        """
        return self._c.request("GET", f"storage/files/{file_id}/download", params=params)

    def get_export_files(self, file_id: str, **params: Any) -> Any:
        """Export a note as a Word document

        ``GET /storage/files/{file_id}/export``
        """
        return self._c.request("GET", f"storage/files/{file_id}/export", params=params)

    def export_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Save a note's Word export into Drive

        ``POST /storage/files/{file_id}/export``
        """
        return self._c.request("POST", f"storage/files/{file_id}/export", json=json, params=params)

    def link_mention_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Link an unlinked mention in a note

        ``POST /storage/files/{file_id}/link-mention``
        """
        return self._c.request("POST", f"storage/files/{file_id}/link-mention", json=json, params=params)

    def opened_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Record that you opened this file

        ``POST /storage/files/{file_id}/opened``
        """
        return self._c.request("POST", f"storage/files/{file_id}/opened", json=json, params=params)

    def get_pages_files(self, file_id: str, **params: Any) -> Any:
        """An office file's first pages, as pictures

        ``GET /storage/files/{file_id}/pages``
        """
        return self._c.request("GET", f"storage/files/{file_id}/pages", params=params)

    def get_pages(self, file_id: str, number: str, **params: Any) -> Any:
        """One drawn page of an office file, as a WebP

        ``GET /storage/files/{file_id}/pages/{number}``
        """
        return self._c.request("GET", f"storage/files/{file_id}/pages/{number}", params=params)

    def get_preview_files(self, file_id: str, **params: Any) -> Any:
        """Read a Word document in the app

        ``GET /storage/files/{file_id}/preview``
        """
        return self._c.request("GET", f"storage/files/{file_id}/preview", params=params)

    def delete_public_image_files(self, file_id: str, **params: Any) -> Any:
        """Turn off a file's public image link

        ``DELETE /storage/files/{file_id}/public-image``
        """
        return self._c.request("DELETE", f"storage/files/{file_id}/public-image", params=params)

    def public_image_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Turn on a file's public image link (a logo in a mail signature)

        ``POST /storage/files/{file_id}/public-image``
        """
        return self._c.request("POST", f"storage/files/{file_id}/public-image", json=json, params=params)

    def purge_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Permanently delete a trashed file (releases quota + ref_count)

        ``POST /storage/files/{file_id}/purge``
        """
        return self._c.request("POST", f"storage/files/{file_id}/purge", json=json, params=params)

    def get_raw_files(self, file_id: str, **params: Any) -> Any:
        """Redirect to the bytes

        ``GET /storage/files/{file_id}/raw``
        """
        return self._c.request("GET", f"storage/files/{file_id}/raw", params=params)

    def get_renditions(self, file_id: str, size: str, **params: Any) -> Any:
        """A file's card picture or an image's large copy, from our origin

        ``GET /storage/files/{file_id}/renditions/{size}``
        """
        return self._c.request("GET", f"storage/files/{file_id}/renditions/{size}", params=params)

    def restore_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Restore a file from trash

        ``POST /storage/files/{file_id}/restore``
        """
        return self._c.request("POST", f"storage/files/{file_id}/restore", json=json, params=params)

    def to_note_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Turn a Word document into a note

        ``POST /storage/files/{file_id}/to-note``
        """
        return self._c.request("POST", f"storage/files/{file_id}/to-note", json=json, params=params)

    def get_usage_files(self, file_id: str, **params: Any) -> Any:
        """Where this file is used right now

        ``GET /storage/files/{file_id}/usage``
        """
        return self._c.request("GET", f"storage/files/{file_id}/usage", params=params)

    def get_versions_files(self, file_id: str, **params: Any) -> Any:
        """A file's version history

        ``GET /storage/files/{file_id}/versions``
        """
        return self._c.request("GET", f"storage/files/{file_id}/versions", params=params)

    def get_versions(self, file_id: str, version_id: str, **params: Any) -> Any:
        """Read one historical version

        ``GET /storage/files/{file_id}/versions/{version_id}``
        """
        return self._c.request("GET", f"storage/files/{file_id}/versions/{version_id}", params=params)

    def get_folder_zips(self, zip_id: str, **params: Any) -> Any:
        """Follow a folder's background ZIP, and get its download link

        ``GET /storage/folder-zips/{zip_id}``
        """
        return self._c.request("GET", f"storage/folder-zips/{zip_id}", params=params)

    def list_folders(self, **params: Any) -> Any:
        """List folders (by parent)

        ``GET /storage/folders``
        """
        return self._c.request("GET", "storage/folders", params=params)

    def create_folders(self, *, json: Any = None, **params: Any) -> Any:
        """Create a folder

        ``POST /storage/folders``
        """
        return self._c.request("POST", "storage/folders", json=json, params=params)

    def delete_folders(self, folder_id: str, **params: Any) -> Any:
        """Soft-delete a folder (to trash)

        ``DELETE /storage/folders/{folder_id}``
        """
        return self._c.request("DELETE", f"storage/folders/{folder_id}", params=params)

    def get_folders(self, folder_id: str, **params: Any) -> Any:
        """Read one folder

        ``GET /storage/folders/{folder_id}``
        """
        return self._c.request("GET", f"storage/folders/{folder_id}", params=params)

    def update_folders(self, folder_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename and/or move a folder

        ``PATCH /storage/folders/{folder_id}``
        """
        return self._c.request("PATCH", f"storage/folders/{folder_id}", json=json, params=params)

    def get_download_folders(self, folder_id: str, **params: Any) -> Any:
        """Download a folder (recursively) as a .zip

        ``GET /storage/folders/{folder_id}/download``
        """
        return self._c.request("GET", f"storage/folders/{folder_id}/download", params=params)

    def purge_folders(self, folder_id: str, *, json: Any = None, **params: Any) -> Any:
        """Permanently delete a trashed folder (and its whole subtree)

        ``POST /storage/folders/{folder_id}/purge``
        """
        return self._c.request("POST", f"storage/folders/{folder_id}/purge", json=json, params=params)

    def restore_folders(self, folder_id: str, *, json: Any = None, **params: Any) -> Any:
        """Restore a folder from trash

        ``POST /storage/folders/{folder_id}/restore``
        """
        return self._c.request("POST", f"storage/folders/{folder_id}/restore", json=json, params=params)

    def list_media(self, **params: Any) -> Any:
        """Images and video across every folder

        ``GET /storage/media``
        """
        return self._c.request("GET", "storage/media", params=params)

    def create_move_drive(self, *, json: Any = None, **params: Any) -> Any:
        """Move items between the Shared drive and My drive

        ``POST /storage/move-drive``
        """
        return self._c.request("POST", "storage/move-drive", json=json, params=params)

    def create_notes(self, *, json: Any = None, **params: Any) -> Any:
        """Create a note

        ``POST /storage/notes``
        """
        return self._c.request("POST", "storage/notes", json=json, params=params)

    def list_recent(self, **params: Any) -> Any:
        """The files you opened most recently

        ``GET /storage/recent``
        """
        return self._c.request("GET", "storage/recent", params=params)

    def list_search(self, **params: Any) -> Any:
        """Search own + discoverable (non-mature) files

        ``GET /storage/search``
        """
        return self._c.request("GET", "storage/search", params=params)

    def list_templates(self, **params: Any) -> Any:
        """List templates

        ``GET /storage/templates``
        """
        return self._c.request("GET", "storage/templates", params=params)

    def create_templates(self, *, json: Any = None, **params: Any) -> Any:
        """Save something as a template

        ``POST /storage/templates``
        """
        return self._c.request("POST", "storage/templates", json=json, params=params)

    def delete_templates(self, template_id: str, **params: Any) -> Any:
        """Delete a template

        ``DELETE /storage/templates/{template_id}``
        """
        return self._c.request("DELETE", f"storage/templates/{template_id}", params=params)

    def update_templates(self, template_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename or update a template

        ``PATCH /storage/templates/{template_id}``
        """
        return self._c.request("PATCH", f"storage/templates/{template_id}", json=json, params=params)

    def apply_templates(self, template_id: str, *, json: Any = None, **params: Any) -> Any:
        """Make something from a template

        ``POST /storage/templates/{template_id}/apply``
        """
        return self._c.request("POST", f"storage/templates/{template_id}/apply", json=json, params=params)

    def publish_templates(self, template_id: str, *, json: Any = None, **params: Any) -> Any:
        """Who may see this template

        ``POST /storage/templates/{template_id}/publish``
        """
        return self._c.request("POST", f"storage/templates/{template_id}/publish", json=json, params=params)

    def get_versions_templates(self, template_id: str, **params: Any) -> Any:
        """A template's version history

        ``GET /storage/templates/{template_id}/versions``
        """
        return self._c.request("GET", f"storage/templates/{template_id}/versions", params=params)

    def versions_templates(self, template_id: str, *, json: Any = None, **params: Any) -> Any:
        """Cut a new version

        ``POST /storage/templates/{template_id}/versions``
        """
        return self._c.request("POST", f"storage/templates/{template_id}/versions", json=json, params=params)

    def list_trash(self, **params: Any) -> Any:
        """List what is in Trash - folders, files, tables and boards

        ``GET /storage/trash``
        """
        return self._c.request("GET", "storage/trash", params=params)

    def list_usage(self, **params: Any) -> Any:
        """Storage usage + effective quota

        ``GET /storage/usage``
        """
        return self._c.request("GET", "storage/usage", params=params)


class SyncOps(_Namespace):
    """1 operations."""

    def list_delta(self, **params: Any) -> Any:
        """The change feed - everything that changed in one tenant, in order

        ``GET /storage/delta``
        """
        return self._c.request("GET", "storage/delta", params=params)


class TablesOps(_Namespace):
    """36 operations."""

    def list_tables(self, **params: Any) -> Any:
        """List tables

        ``GET /tables``
        """
        return self._c.request("GET", "tables", params=params)

    def create_tables(self, *, json: Any = None, **params: Any) -> Any:
        """Create a table

        ``POST /tables``
        """
        return self._c.request("POST", "tables", json=json, params=params)

    def delete_fields(self, field_id: str, **params: Any) -> Any:
        """Delete a column and its data

        ``DELETE /tables/fields/{field_id}``
        """
        return self._c.request("DELETE", f"tables/fields/{field_id}", params=params)

    def update_fields(self, field_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change a column

        ``PATCH /tables/fields/{field_id}``
        """
        return self._c.request("PATCH", f"tables/fields/{field_id}", json=json, params=params)

    def change_type_fields(self, field_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change a column's type, converting what it can

        ``POST /tables/fields/{field_id}/change_type``
        """
        return self._c.request("POST", f"tables/fields/{field_id}/change_type", json=json, params=params)

    def duplicate_fields(self, field_id: str, *, json: Any = None, **params: Any) -> Any:
        """Copy a column, its settings and its values

        ``POST /tables/fields/{field_id}/duplicate``
        """
        return self._c.request("POST", f"tables/fields/{field_id}/duplicate", json=json, params=params)

    def restore_fields(self, field_id: str, *, json: Any = None, **params: Any) -> Any:
        """Put a deleted column back, under its original id

        ``POST /tables/fields/{field_id}/restore``
        """
        return self._c.request("POST", f"tables/fields/{field_id}/restore", json=json, params=params)

    def revert_type_fields(self, field_id: str, *, json: Any = None, **params: Any) -> Any:
        """Undo the last type change, values and all

        ``POST /tables/fields/{field_id}/revert_type``
        """
        return self._c.request("POST", f"tables/fields/{field_id}/revert_type", json=json, params=params)

    def get_query_files(self, file_id: str, **params: Any) -> Any:
        """Query a spreadsheet's or CSV's rows

        ``GET /tables/files/{file_id}/query``
        """
        return self._c.request("GET", f"tables/files/{file_id}/query", params=params)

    def create_from_csv(self, *, json: Any = None, **params: Any) -> Any:
        """Create a populated table from a CSV preview

        ``POST /tables/from-csv``
        """
        return self._c.request("POST", "tables/from-csv", json=json, params=params)

    def delete_rows(self, row_id: str, **params: Any) -> Any:
        """Delete a row

        ``DELETE /tables/rows/{row_id}``
        """
        return self._c.request("DELETE", f"tables/rows/{row_id}", params=params)

    def update_rows(self, row_id: str, *, json: Any = None, **params: Any) -> Any:
        """Edit a row

        ``PATCH /tables/rows/{row_id}``
        """
        return self._c.request("PATCH", f"tables/rows/{row_id}", json=json, params=params)

    def delete_views(self, view_id: str, **params: Any) -> Any:
        """Delete a view

        ``DELETE /tables/views/{view_id}``
        """
        return self._c.request("DELETE", f"tables/views/{view_id}", params=params)

    def update_views(self, view_id: str, *, json: Any = None, **params: Any) -> Any:
        """Update a view

        ``PATCH /tables/views/{view_id}``
        """
        return self._c.request("PATCH", f"tables/views/{view_id}", json=json, params=params)

    def delete_tables(self, table_id: str, **params: Any) -> Any:
        """Move a table to trash

        ``DELETE /tables/{table_id}``
        """
        return self._c.request("DELETE", f"tables/{table_id}", params=params)

    def get_tables(self, table_id: str, **params: Any) -> Any:
        """Open a table - its full schema

        ``GET /tables/{table_id}``
        """
        return self._c.request("GET", f"tables/{table_id}", params=params)

    def update_tables(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename, move, describe or restore a table

        ``PATCH /tables/{table_id}``
        """
        return self._c.request("PATCH", f"tables/{table_id}", json=json, params=params)

    def get_export_tables(self, table_id: str, **params: Any) -> Any:
        """Download the table as CSV or XLSX

        ``GET /tables/{table_id}/export``
        """
        return self._c.request("GET", f"tables/{table_id}/export", params=params)

    def export_tables(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Save the table as a CSV or XLSX file in Drive

        ``POST /tables/{table_id}/export``
        """
        return self._c.request("POST", f"tables/{table_id}/export", json=json, params=params)

    def fields_tables(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Add a column

        ``POST /tables/{table_id}/fields``
        """
        return self._c.request("POST", f"tables/{table_id}/fields", json=json, params=params)

    def bulk_delete_fields(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Delete many columns in one call

        ``POST /tables/{table_id}/fields/bulk_delete``
        """
        return self._c.request("POST", f"tables/{table_id}/fields/bulk_delete", json=json, params=params)

    def get_files_tables(self, table_id: str, **params: Any) -> Any:
        """Name the files this table's cells hold

        ``GET /tables/{table_id}/files``
        """
        return self._c.request("GET", f"tables/{table_id}/files", params=params)

    def get_files(self, table_id: str, file_id: str, **params: Any) -> Any:
        """A file this table's cells hold, from our origin

        ``GET /tables/{table_id}/files/{file_id}``
        """
        return self._c.request("GET", f"tables/{table_id}/files/{file_id}", params=params)

    def get_preview_files(self, table_id: str, file_id: str, **params: Any) -> Any:
        """Read a Word document a table's cell holds

        ``GET /tables/{table_id}/files/{file_id}/preview``
        """
        return self._c.request("GET", f"tables/{table_id}/files/{file_id}/preview", params=params)

    def import_tables(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Import rows and the new columns they need, all or nothing

        ``POST /tables/{table_id}/import``
        """
        return self._c.request("POST", f"tables/{table_id}/import", json=json, params=params)

    def purge_tables(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Permanently delete a table that is in Trash

        ``POST /tables/{table_id}/purge``
        """
        return self._c.request("POST", f"tables/{table_id}/purge", json=json, params=params)

    def get_query_tables(self, table_id: str, **params: Any) -> Any:
        """Query rows (filter, group, aggregate)

        ``GET /tables/{table_id}/query``
        """
        return self._c.request("GET", f"tables/{table_id}/query", params=params)

    def get_rows_tables(self, table_id: str, **params: Any) -> Any:
        """List rows

        ``GET /tables/{table_id}/rows``
        """
        return self._c.request("GET", f"tables/{table_id}/rows", params=params)

    def rows_tables(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Add a row

        ``POST /tables/{table_id}/rows``
        """
        return self._c.request("POST", f"tables/{table_id}/rows", json=json, params=params)

    def bulk_create_rows(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Add many rows in one call

        ``POST /tables/{table_id}/rows/bulk_create``
        """
        return self._c.request("POST", f"tables/{table_id}/rows/bulk_create", json=json, params=params)

    def bulk_delete_rows(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Delete many rows in one call

        ``POST /tables/{table_id}/rows/bulk_delete``
        """
        return self._c.request("POST", f"tables/{table_id}/rows/bulk_delete", json=json, params=params)

    def update_bulk_update_rows(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Edit many rows in one call

        ``PATCH /tables/{table_id}/rows/bulk_update``
        """
        return self._c.request("PATCH", f"tables/{table_id}/rows/bulk_update", json=json, params=params)

    def restore_rows(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Restore deleted rows as themselves

        ``POST /tables/{table_id}/rows/restore``
        """
        return self._c.request("POST", f"tables/{table_id}/rows/restore", json=json, params=params)

    def update_title_field_tables(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Choose the column that labels this table's rows

        ``PATCH /tables/{table_id}/title-field``
        """
        return self._c.request("PATCH", f"tables/{table_id}/title-field", json=json, params=params)

    def get_usage_tables(self, table_id: str, **params: Any) -> Any:
        """Where this table is used right now

        ``GET /tables/{table_id}/usage``
        """
        return self._c.request("GET", f"tables/{table_id}/usage", params=params)

    def views_tables(self, table_id: str, *, json: Any = None, **params: Any) -> Any:
        """Save a view of a table

        ``POST /tables/{table_id}/views``
        """
        return self._c.request("POST", f"tables/{table_id}/views", json=json, params=params)


class TasksOps(_Namespace):
    """15 operations."""

    def list_tasks(self, **params: Any) -> Any:
        """List tasks

        ``GET /tasks``
        """
        return self._c.request("GET", "tasks", params=params)

    def create_tasks(self, *, json: Any = None, **params: Any) -> Any:
        """Create a task

        ``POST /tasks``
        """
        return self._c.request("POST", "tasks", json=json, params=params)

    def list_lists(self, **params: Any) -> Any:
        """List task lists

        ``GET /tasks/lists``
        """
        return self._c.request("GET", "tasks/lists", params=params)

    def create_lists(self, *, json: Any = None, **params: Any) -> Any:
        """Create a task list

        ``POST /tasks/lists``
        """
        return self._c.request("POST", "tasks/lists", json=json, params=params)

    def delete_lists(self, list_id: str, **params: Any) -> Any:
        """Delete a task list

        ``DELETE /tasks/lists/{list_id}``
        """
        return self._c.request("DELETE", f"tasks/lists/{list_id}", params=params)

    def get_lists(self, list_id: str, **params: Any) -> Any:
        """Read one task list

        ``GET /tasks/lists/{list_id}``
        """
        return self._c.request("GET", f"tasks/lists/{list_id}", params=params)

    def update_lists(self, list_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename, reorder, archive or unarchive a task list

        ``PATCH /tasks/lists/{list_id}``
        """
        return self._c.request("PATCH", f"tasks/lists/{list_id}", json=json, params=params)

    def delete_tasks(self, task_id: str, **params: Any) -> Any:
        """Move a task to trash

        ``DELETE /tasks/{task_id}``
        """
        return self._c.request("DELETE", f"tasks/{task_id}", params=params)

    def get_tasks(self, task_id: str, **params: Any) -> Any:
        """Read one task

        ``GET /tasks/{task_id}``
        """
        return self._c.request("GET", f"tasks/{task_id}", params=params)

    def update_tasks(self, task_id: str, *, json: Any = None, **params: Any) -> Any:
        """Update a task

        ``PATCH /tasks/{task_id}``
        """
        return self._c.request("PATCH", f"tasks/{task_id}", json=json, params=params)

    def get_comments_tasks(self, task_id: str, **params: Any) -> Any:
        """A task's comments and history

        ``GET /tasks/{task_id}/comments``
        """
        return self._c.request("GET", f"tasks/{task_id}/comments", params=params)

    def comments_tasks(self, task_id: str, *, json: Any = None, **params: Any) -> Any:
        """Comment on a task

        ``POST /tasks/{task_id}/comments``
        """
        return self._c.request("POST", f"tasks/{task_id}/comments", json=json, params=params)

    def delete_comments(self, task_id: str, comment_id: str, **params: Any) -> Any:
        """Delete a comment

        ``DELETE /tasks/{task_id}/comments/{comment_id}``
        """
        return self._c.request("DELETE", f"tasks/{task_id}/comments/{comment_id}", params=params)

    def update_comments(self, task_id: str, comment_id: str, *, json: Any = None, **params: Any) -> Any:
        """Edit your comment

        ``PATCH /tasks/{task_id}/comments/{comment_id}``
        """
        return self._c.request("PATCH", f"tasks/{task_id}/comments/{comment_id}", json=json, params=params)

    def purge_tasks(self, task_id: str, *, json: Any = None, **params: Any) -> Any:
        """Delete a trashed task permanently

        ``POST /tasks/{task_id}/purge``
        """
        return self._c.request("POST", f"tasks/{task_id}/purge", json=json, params=params)


class UploadOps(_Namespace):
    """9 operations."""

    def complete_content(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Replace an existing file's content (step 2) - commit the staged bytes

        ``POST /storage/files/{file_id}/content/complete``
        """
        return self._c.request("POST", f"storage/files/{file_id}/content/complete", json=json, params=params)

    def parts_content(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Replace an existing file's content (step 2, resumable) - one presigned part

        ``POST /storage/files/{file_id}/content/parts``
        """
        return self._c.request("POST", f"storage/files/{file_id}/content/parts", json=json, params=params)

    def upload_content(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Replace an existing file's content (step 1) - reserve + presigned target

        ``POST /storage/files/{file_id}/content/upload``
        """
        return self._c.request("POST", f"storage/files/{file_id}/content/upload", json=json, params=params)

    def list_upload_limits(self, **params: Any) -> Any:
        """The upload limits, before a file is picked

        ``GET /storage/upload-limits``
        """
        return self._c.request("GET", "storage/upload-limits", params=params)

    def create_uploads(self, *, json: Any = None, **params: Any) -> Any:
        """Initiate an upload (reserve quota + presigned target)

        ``POST /storage/uploads``
        """
        return self._c.request("POST", "storage/uploads", json=json, params=params)

    def abort_uploads(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Give up on a resumable upload

        ``POST /storage/uploads/{file_id}/abort``
        """
        return self._c.request("POST", f"storage/uploads/{file_id}/abort", json=json, params=params)

    def complete_uploads(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Complete an upload (dedup → commit)

        ``POST /storage/uploads/{file_id}/complete``
        """
        return self._c.request("POST", f"storage/uploads/{file_id}/complete", json=json, params=params)

    def get_parts_uploads(self, file_id: str, **params: Any) -> Any:
        """What has arrived for a resumable upload - the parts the server holds

        ``GET /storage/uploads/{file_id}/parts``
        """
        return self._c.request("GET", f"storage/uploads/{file_id}/parts", params=params)

    def parts_uploads(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Get a presigned URL for one part of a resumable upload

        ``POST /storage/uploads/{file_id}/parts``
        """
        return self._c.request("POST", f"storage/uploads/{file_id}/parts", json=json, params=params)


class VideoOps(_Namespace):
    """1 operations."""

    def play_files(self, file_id: str, *, json: Any = None, **params: Any) -> Any:
        """Get a direct URL to play an owned video inline

        ``POST /storage/files/{file_id}/play``
        """
        return self._c.request("POST", f"storage/files/{file_id}/play", json=json, params=params)


class WebhooksOps(_Namespace):
    """12 operations."""

    def list_webhooks(self, **params: Any) -> Any:
        """Your webhooks

        ``GET /webhooks/``
        """
        return self._c.request("GET", "webhooks/", params=params)

    def create_webhooks(self, *, json: Any = None, **params: Any) -> Any:
        """Add a webhook

        ``POST /webhooks/``
        """
        return self._c.request("POST", "webhooks/", json=json, params=params)

    def list_events(self, **params: Any) -> Any:
        """The events a webhook can subscribe to

        ``GET /webhooks/events``
        """
        return self._c.request("GET", "webhooks/events", params=params)

    def delete_webhooks(self, webhook_id: str, **params: Any) -> Any:
        """Delete a webhook

        ``DELETE /webhooks/{webhook_id}``
        """
        return self._c.request("DELETE", f"webhooks/{webhook_id}", params=params)

    def get_webhooks(self, webhook_id: str, **params: Any) -> Any:
        """One webhook

        ``GET /webhooks/{webhook_id}``
        """
        return self._c.request("GET", f"webhooks/{webhook_id}", params=params)

    def update_webhooks(self, webhook_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change a webhook

        ``PATCH /webhooks/{webhook_id}``
        """
        return self._c.request("PATCH", f"webhooks/{webhook_id}", json=json, params=params)

    def get_deliveries_webhooks(self, webhook_id: str, **params: Any) -> Any:
        """The delivery log

        ``GET /webhooks/{webhook_id}/deliveries``
        """
        return self._c.request("GET", f"webhooks/{webhook_id}/deliveries", params=params)

    def redeliver_deliveries(self, webhook_id: str, delivery_id: str, *, json: Any = None, **params: Any) -> Any:
        """Send an event again

        ``POST /webhooks/{webhook_id}/deliveries/{delivery_id}/redeliver``
        """
        return self._c.request(
            "POST", f"webhooks/{webhook_id}/deliveries/{delivery_id}/redeliver", json=json, params=params
        )

    def resume_webhooks(self, webhook_id: str, *, json: Any = None, **params: Any) -> Any:
        """Resume a paused webhook

        ``POST /webhooks/{webhook_id}/resume``
        """
        return self._c.request("POST", f"webhooks/{webhook_id}/resume", json=json, params=params)

    def get_secret_webhooks(self, webhook_id: str, **params: Any) -> Any:
        """Reveal the signing secret

        ``GET /webhooks/{webhook_id}/secret``
        """
        return self._c.request("GET", f"webhooks/{webhook_id}/secret", params=params)

    def secret_webhooks(self, webhook_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rotate the signing secret

        ``POST /webhooks/{webhook_id}/secret``
        """
        return self._c.request("POST", f"webhooks/{webhook_id}/secret", json=json, params=params)

    def test_webhooks(self, webhook_id: str, *, json: Any = None, **params: Any) -> Any:
        """Send a test ping

        ``POST /webhooks/{webhook_id}/test``
        """
        return self._c.request("POST", f"webhooks/{webhook_id}/test", json=json, params=params)


class WorkspacesOps(_Namespace):
    """25 operations."""

    def get_invites(self, token: str, **params: Any) -> Any:
        """What this invitation is for, before accepting it

        ``GET /invites/{token}``
        """
        return self._c.request("GET", f"invites/{token}", params=params)

    def accept_invites(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Join the workspace

        ``POST /invites/{token}/accept``
        """
        return self._c.request("POST", f"invites/{token}/accept", json=json, params=params)

    def decline_invites(self, token: str, *, json: Any = None, **params: Any) -> Any:
        """Decline the invitation

        ``POST /invites/{token}/decline``
        """
        return self._c.request("POST", f"invites/{token}/decline", json=json, params=params)

    def list_personal_space(self, **params: Any) -> Any:
        """Your own space

        ``GET /personal-space``
        """
        return self._c.request("GET", "personal-space", params=params)

    def update_personal_space(self, *, json: Any = None, **params: Any) -> Any:
        """Rename your own space

        ``PATCH /personal-space``
        """
        return self._c.request("PATCH", "personal-space", json=json, params=params)

    def list_workspaces(self, **params: Any) -> Any:
        """The workspaces you belong to, with your role in each

        ``GET /workspaces``
        """
        return self._c.request("GET", "workspaces", params=params)

    def list_capabilities(self, **params: Any) -> Any:
        """What the space this request acts in allows

        ``GET /workspaces/capabilities``
        """
        return self._c.request("GET", "workspaces/capabilities", params=params)

    def delete_workspaces(self, workspace_id: str, **params: Any) -> Any:
        """Delete a workspace and everything in it

        ``DELETE /workspaces/{workspace_id}``
        """
        return self._c.request("DELETE", f"workspaces/{workspace_id}", params=params)

    def get_workspaces(self, workspace_id: str, **params: Any) -> Any:
        """Read one workspace

        ``GET /workspaces/{workspace_id}``
        """
        return self._c.request("GET", f"workspaces/{workspace_id}", params=params)

    def update_workspaces(self, workspace_id: str, *, json: Any = None, **params: Any) -> Any:
        """Rename a workspace, set its time zone, or change its storage limit (owner only)

        ``PATCH /workspaces/{workspace_id}``
        """
        return self._c.request("PATCH", f"workspaces/{workspace_id}", json=json, params=params)

    def get_dashboard_workspaces(self, workspace_id: str, **params: Any) -> Any:
        """The Workspace view of Home, for its Owner and Admins

        ``GET /workspaces/{workspace_id}/dashboard``
        """
        return self._c.request("GET", f"workspaces/{workspace_id}/dashboard", params=params)

    def get_invites_workspaces(self, workspace_id: str, **params: Any) -> Any:
        """Outstanding invitations

        ``GET /workspaces/{workspace_id}/invites``
        """
        return self._c.request("GET", f"workspaces/{workspace_id}/invites", params=params)

    def invites_workspaces(self, workspace_id: str, *, json: Any = None, **params: Any) -> Any:
        """Invite somebody by email

        ``POST /workspaces/{workspace_id}/invites``
        """
        return self._c.request("POST", f"workspaces/{workspace_id}/invites", json=json, params=params)

    def delete_invites(self, workspace_id: str, invite_id: str, **params: Any) -> Any:
        """Revoke an invitation before it is accepted

        ``DELETE /workspaces/{workspace_id}/invites/{invite_id}``
        """
        return self._c.request("DELETE", f"workspaces/{workspace_id}/invites/{invite_id}", params=params)

    def get_link_invites(self, workspace_id: str, invite_id: str, **params: Any) -> Any:
        """The link a pending invitation's email carries

        ``GET /workspaces/{workspace_id}/invites/{invite_id}/link``
        """
        return self._c.request("GET", f"workspaces/{workspace_id}/invites/{invite_id}/link", params=params)

    def resend_invites(self, workspace_id: str, invite_id: str, *, json: Any = None, **params: Any) -> Any:
        """Send a pending invitation again

        ``POST /workspaces/{workspace_id}/invites/{invite_id}/resend``
        """
        return self._c.request(
            "POST", f"workspaces/{workspace_id}/invites/{invite_id}/resend", json=json, params=params
        )

    def leave_workspaces(self, workspace_id: str, *, json: Any = None, **params: Any) -> Any:
        """Leave a workspace

        ``POST /workspaces/{workspace_id}/leave``
        """
        return self._c.request("POST", f"workspaces/{workspace_id}/leave", json=json, params=params)

    def get_manage_workspaces(self, workspace_id: str, **params: Any) -> Any:
        """The Manage workspace page's data

        ``GET /workspaces/{workspace_id}/manage``
        """
        return self._c.request("GET", f"workspaces/{workspace_id}/manage", params=params)

    def update_manage_workspaces(self, workspace_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change the workspace's AI, indexing, caps and chat file rule

        ``PATCH /workspaces/{workspace_id}/manage``
        """
        return self._c.request("PATCH", f"workspaces/{workspace_id}/manage", json=json, params=params)

    def get_members_workspaces(self, workspace_id: str, **params: Any) -> Any:
        """Who is in this workspace, and with what role

        ``GET /workspaces/{workspace_id}/members``
        """
        return self._c.request("GET", f"workspaces/{workspace_id}/members", params=params)

    def delete_members(self, workspace_id: str, user_id: str, **params: Any) -> Any:
        """Remove somebody from the workspace

        ``DELETE /workspaces/{workspace_id}/members/{user_id}``
        """
        return self._c.request("DELETE", f"workspaces/{workspace_id}/members/{user_id}", params=params)

    def update_members(self, workspace_id: str, user_id: str, *, json: Any = None, **params: Any) -> Any:
        """Change somebody's role

        ``PATCH /workspaces/{workspace_id}/members/{user_id}``
        """
        return self._c.request("PATCH", f"workspaces/{workspace_id}/members/{user_id}", json=json, params=params)

    def update_storage_cap_members(self, workspace_id: str, user_id: str, *, json: Any = None, **params: Any) -> Any:
        """Set a member's storage limit in this workspace

        ``PATCH /workspaces/{workspace_id}/members/{user_id}/storage-cap``
        """
        return self._c.request(
            "PATCH", f"workspaces/{workspace_id}/members/{user_id}/storage-cap", json=json, params=params
        )

    def get_storage_by_person_workspaces(self, workspace_id: str, **params: Any) -> Any:
        """Storage by person

        ``GET /workspaces/{workspace_id}/storage-by-person``
        """
        return self._c.request("GET", f"workspaces/{workspace_id}/storage-by-person", params=params)

    def transfer_ownership_workspaces(self, workspace_id: str, *, json: Any = None, **params: Any) -> Any:
        """Hand ownership to another member

        ``POST /workspaces/{workspace_id}/transfer-ownership``
        """
        return self._c.request("POST", f"workspaces/{workspace_id}/transfer-ownership", json=json, params=params)


#: Attribute name -> namespace class. `FlowpyDisk.__init__` walks this, so a
#: regeneration that adds a tag adds a namespace with no other edit.
NAMESPACES = {
    "account": AccountOps,
    "auth": AuthOps,
    "backups": BackupsOps,
    "banners": BannersOps,
    "billing": BillingOps,
    "booking": BookingOps,
    "calendar": CalendarOps,
    "canvas": CanvasOps,
    "collab": CollabOps,
    "comments": CommentsOps,
    "connections": ConnectionsOps,
    "drive_imports": DriveImportsOps,
    "forms": FormsOps,
    "graph": GraphOps,
    "inbound_webhooks": InboundWebhooksOps,
    "insights": InsightsOps,
    "knowledge": KnowledgeOps,
    "mail": MailOps,
    "market": MarketOps,
    "notifications": NotificationsOps,
    "ops": OpsOps,
    "public": PublicOps,
    "publishing": PublishingOps,
    "rag": RagOps,
    "reach": ReachOps,
    "sharing": SharingOps,
    "storage": StorageOps,
    "sync": SyncOps,
    "tables": TablesOps,
    "tasks": TasksOps,
    "upload": UploadOps,
    "video": VideoOps,
    "webhooks": WebhooksOps,
    "workspaces": WorkspacesOps,
}

#: Older attribute name -> the namespace it is now. `FlowpyDisk.__init__`
#: sets each one to the same object, so both names reach the same methods.
ALIASES = {}
