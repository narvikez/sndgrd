import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *


message = Mail()

message.to = [
    To(
        email="tm_sg@intelligentbee.com",
        name="tm_sg",
        p=0
    ),
]
message.from_email = From(
    email="s.krisztianr@gmail.com",
    name="Simon Krisztian",
    p=1
)

message.reply_to = ReplyTo(
    email="customer_service@example.com",
    name="Example Customer Service Team"
)

message.subject = Subject("Sendgrid API v3")

message.content = [
    Content(
        mime_type="text/html",
        content="<p>Hello from Twilio SendGrid!</p><p>Sending with the email service trusted by developers and marketers for <strong>time-savings</strong>, <strong>scalability</strong>, and <strong>delivery expertise</strong>.</p><p>%open-track%</p>"
    )]

message.batch_id = BatchId("AsdFgHjklQweRTYuIopzXcVBNm0aSDfGHjklmZcVbNMqWert1znmOP2asDFjkl")

message.asm = Asm(
    group_id=GroupId(12345),
    groups_to_display=GroupsToDisplay([12345])
)

message.ip_pool_name = IpPoolName("transactional email")

message.mail_settings = MailSettings(
    bypass_list_management=BypassListManagement(False),
    footer_settings=FooterSettings(False),
    sandbox_mode=SandBoxMode(False)
)

message.tracking_settings = TrackingSettings(
    click_tracking=ClickTracking(
        enable=True,
        enable_text=False
    ),
    open_tracking=OpenTracking(
        enable=True,
        substitution_tag=OpenTrackingSubstitutionTag("%open-track%")
    ),
    subscription_tracking=SubscriptionTracking(False)
)

sendgrid_client = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
response = sendgrid_client.send(message)

print(response.status_code)
print(response.body)
print(response.headers)