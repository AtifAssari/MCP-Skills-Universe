---
rating: ⭐⭐
title: checkout-payments
url: https://skills.sh/santiagoxor/pintureria-digital/checkout-payments
---

# checkout-payments

skills/santiagoxor/pintureria-digital/checkout-payments
checkout-payments
Installation
$ npx skills add https://github.com/santiagoxor/pintureria-digital --skill checkout-payments
SKILL.md
Checkout and Payments
Quick Start

When working with checkout:

Validate cart data before creating order
Validate shipping address
Create order in database
Integrate with MercadoPago
Handle payment webhooks
Update order status
Key Files
src/app/checkout/ - Checkout pages
src/components/Checkout/ - Checkout components
src/lib/integrations/mercadopago/ - MercadoPago integration
src/lib/business/orders/ - Order logic
src/hooks/useCheckout.ts - Checkout hook
Common Patterns
Create Order
import { createOrder } from '@/lib/business/orders/order-service';
import { createPayment } from '@/lib/integrations/mercadopago';

export async function POST(request: NextRequest) {
  const { items, shippingAddress, paymentMethod } = await request.json();
  
  const order = await createOrder({
    items,
    shippingAddress,
    status: 'pending_payment',
  });
  
  const payment = await createPayment({
    transaction_amount: order.total,
    description: `Orden #${order.id}`,
    payer: {
      email: order.customer_email,
    },
  });
  
  await updateOrder(order.id, {
    payment_id: payment.id,
    payment_status: 'pending',
  });
  
  return NextResponse.json({ order, payment });
}

Validate Address
import { validateAddress } from '@/lib/business/logistics/address-validation';

const validation = await validateAddress({
  street: 'Av. Corrientes 1234',
  city: 'Buenos Aires',
  postalCode: 'C1043AAX',
  country: 'AR',
});

if (!validation.isValid) {
  return { errors: validation.errors };
}

MercadoPago Wallet
import { initMercadoPago, Wallet } from '@mercadopago/sdk-react';

function CheckoutPayment() {
  const [paymentData, setPaymentData] = useState(null);
  
  useEffect(() => {
    initMercadoPago('YOUR_PUBLIC_KEY');
  }, []);
  
  return (
    <Wallet
      initialization={{ preferenceId: paymentData?.preference_id }}
      onSubmit={onSubmit}
    />
  );
}

Order States
pending_payment - Waiting for payment
paid - Paid
processing - Processing
shipped - Shipped
delivered - Delivered
cancelled - Cancelled
refunded - Refunded
Weekly Installs
39
Repository
santiagoxor/pin…-digital
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn