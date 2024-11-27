-- retrieve customerName, email, PhoneNumber.
SELECT customerName, email, PhoneNumber FROM customer;

-- retrieve customerName, email, PhoneNumber using where clause.
SELECT customerName, email, PhoneNumber FROM customer
WHERE customerAddress = "Kisii";

-- retrieve customerID, TotalAmount using where clause.
SELECT customerID, TotalAmount FROM bills
WHERE status = "unpaid";

-- retrieve customerID, TotalAmount, CategoryID using where clause.
SELECT customerID, TotalAmount, CategoryID FROM bills
WHERE status = "paid";

-- retrieve customerID, status using where, between & and clauses.
SELECT customerID, status FROM bills
WHERE BillDate BETWEEN "2024-11-01" AND "2024-11-30";

-- retrieve billID, itemDescription, LineTotal and arrange in descending order.
SELECT billID, itemDescription, LineTotal from bill_items
ORDER BY LineTotal DESC;

-- retrieve billID, itemDescription, LineTotal and arrange in ascending order.
SELECT billID, itemDescription, LineTotal from bill_items
ORDER BY LineTotal ASC;

-- retrieve billID, itemDescription, LineTotal and filter using where clause and arrange in descending order.
SELECT billID, itemDescription, LineTotal from bill_items
WHERE LineTotal > 100
ORDER BY billID DESC;

-- retrieve PaymentAmount, PaymentMethod using where and like clause.
SELECT PaymentAmount, PaymentMethod FROM payments
WHERE paymentMethod LIKE '%esa%';

-- retrieve CustomerName, CustomerAddress using where and like clause.
SELECT CustomerName, CustomerAddress FROM customer
WHERE CustomerAddress LIKE '%Ki%';
