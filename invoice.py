import random
import starkbank
from starkbank import Invoice
from faker import Faker
from datetime import datetime, timedelta
from logger import logger

faker = Faker('pt_BR')

def create_invoices():
    quantity = random.randint(8, 12)
    invoices = []

    for _ in range(quantity):
        amount = random.randint(10000, 100000)
        due_date = datetime.now() + timedelta(days=7)
        discount_date = due_date - timedelta(days=1)
        name = faker.name()
        tax_id = faker.cpf().replace('.', '').replace('-', '')

        invoice = Invoice(
            amount=amount,
            name=name,
            tax_id=tax_id,
            due=due_date,
            expiration=3600 * 24,
            fine=2.5,
            interest=1.3,
            descriptions=[{"key": "Serviço", "value": "Assinatura mensal"}],
            discounts=[{"percentage": 5, "due": discount_date}],
            tags=["auto-generator", "test"],
            rules=[{
                "key": "allowedTaxIds",
                "value": [tax_id]
            }],
            splits=[]
        )

        invoices.append(invoice)

    created = starkbank.invoice.create(invoices)

    for inv in created:
        logger.info(f"Invoice created: {inv.id} | R${inv.amount / 100:.2f} for {inv.name}")
