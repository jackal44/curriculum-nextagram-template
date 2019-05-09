import braintree
import os

client_token = gateway.client_token.generate({
    "customer_id": a_customer_id
})

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=os.getenv(MERCHANT_ID),
        public_key=os.getenv(PUBLIC_KEY),
        private_key=os.getenv(PRIVATE_KEY)
    )
)
