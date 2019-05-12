import braintree
import os

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        environment=braintree.Environment.Sandbox,
        merchant_id=os.environ.get("MERCHANT_ID"),
        public_key=os.environ.get("PUBLIC_KEY"),
        private_key=os.environ.get("PRIVATE_KEY")
    )
)


def transact(options):
    return gateway.transaction.sale(options)


def find_transaction(id):
    return gateway.transaction.find(id)
