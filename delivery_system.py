class Customer:
    """Represents a customer placing a delivery order."""

    def __init__(self, name, email, address, phone=None, customer_id=None):
        """Initialize a Customer with name, email, address, and optional phone and ID."""
        self._name = name
        self._email = email
        self._address = address
        self._phone = phone
        self._customer_id = customer_id

    # Getter methods
    def get_name(self):
        """Return the customer's name."""
        return self._name

    def get_email(self):
        """Return the customer's email."""
        return self._email

    def get_address(self):
        """Return the customer's delivery address."""
        return self._address

    def get_phone(self):
        """Return the customer's phone number."""
        return self._phone

    def get_customer_id(self):
        """Return the customer's unique ID."""
        return self._customer_id

    # Setter methods
    def set_name(self, name):
        """Set the customer's name."""
        self._name = name

    def set_email(self, email):
        """Set the customer's email."""
        self._email = email

    def set_address(self, address):
        """Set the customer's delivery address."""
        self._address = address

    def set_phone(self, phone):
        """Set the customer's phone number."""
        self._phone = phone

    def set_customer_id(self, customer_id):
        """Set the customer's unique ID."""
        self._customer_id = customer_id

    def validate_order(self):
        """Validate the customer's order details (e.g., ensure all fields are filled)."""
        if not self._name or not self._email or not self._address:
            raise ValueError(
                "Customer name, email, and address must not be empty.")
        if self._email and '@' not in self._email:
            raise ValueError("Invalid email format.")
        return True


class Order:
    """Represents a delivery order with items and delivery details."""

    def __init__(self, order_number, reference_number, delivery_date, customer, items=None):
        """Initialize an Order with order number, reference, date, customer, and optional items list."""
        self._order_number = order_number
        self._reference_number = reference_number
        self._delivery_date = delivery_date
        self._customer = customer
        self._items = items if items else []
        self._status = "Pending"

    # Getter methods
    def get_order_number(self):
        """Return the order number."""
        return self._order_number

    def get_reference_number(self):
        """Return the reference number."""
        return self._reference_number

    def get_delivery_date(self):
        """Return the delivery date."""
        return self._delivery_date

    def get_customer(self):
        """Return the associated customer."""
        return self._customer

    def get_items(self):
        """Return the list of items in the order."""
        return self._items

    def get_status(self):
        """Return the order status."""
        return self._status

    # Setter methods
    def set_order_number(self, order_number):
        """Set the order number."""
        self._order_number = order_number

    def set_reference_number(self, reference_number):
        """Set the reference number."""
        self._reference_number = reference_number

    def set_delivery_date(self, delivery_date):
        """Set the delivery date."""
        self._delivery_date = delivery_date

    def set_customer(self, customer):
        """Set the associated customer."""
        self._customer = customer

    def set_items(self, items):
        """Set the list of items in the order."""
        self._items = items

    def set_status(self, status):
        """Set the order status."""
        self._status = status

    def calculate_total(self):
        """Calculate the total price of all items in the order."""
        total = sum(item.get_total_price() for item in self._items)
        return total


class Delivery:
    """Represents delivery details including method, package dimensions, and weight."""

    def __init__(self, method, dimensions, weight, order, tracking_number=None):
        """Initialize a Delivery with method, dimensions, weight, order, and optional tracking number."""
        self._method = method
        self._dimensions = dimensions
        self._weight = weight
        self._order = order
        self._tracking_number = tracking_number

    # Getter methods
    def get_method(self):
        """Return the delivery method."""
        return self._method

    def get_dimensions(self):
        """Return the package dimensions."""
        return self._dimensions

    def get_weight(self):
        """Return the total weight."""
        return self._weight

    def get_order(self):
        """Return the associated order."""
        return self._order

    def get_tracking_number(self):
        """Return the tracking number."""
        return self._tracking_number

    # Setter methods
    def set_method(self, method):
        """Set the delivery method."""
        self._method = method

    def set_dimensions(self, dimensions):
        """Set the package dimensions."""
        self._dimensions = dimensions

    def set_weight(self, weight):
        """Set the total weight."""
        self._weight = weight

    def set_order(self, order):
        """Set the associated order."""
        self._order = order

    def set_tracking_number(self, tracking_number):
        """Set the tracking number."""
        self._tracking_number = tracking_number

    def update_status(self):
        """Update the delivery status based on tracking information."""
        if self._tracking_number:
            current_status = self._order.get_status()
            if current_status == "Pending":
                self._order.set_status("In Transit")
            elif current_status == "In Transit":
                self._order.set_status("Delivered")
            else:
                self._order.set_status("Delivered")  # Final state
        else:
            raise ValueError("Tracking number is required to update status.")


class Item:
    """Represents an individual item in a delivery order."""

    def __init__(self, item_code, description, quantity, unit_price, total_price):
        """Initialize an Item with code, description, quantity, unit price, and total price."""
        self._item_code = item_code
        self._description = description
        self._quantity = quantity
        self._unit_price = unit_price
        self._total_price = total_price

    # Getter methods
    def get_item_code(self):
        """Return the item code."""
        return self._item_code

    def get_description(self):
        """Return the item description."""
        return self._description

    def get_quantity(self):
        """Return the quantity of the item."""
        return self._quantity

    def get_unit_price(self):
        """Return the unit price of the item."""
        return self._unit_price

    def get_total_price(self):
        """Return the total price of the item."""
        return self._total_price

    # Setter methods
    def set_item_code(self, item_code):
        """Set the item code."""
        self._item_code = item_code

    def set_description(self, description):
        """Set the item description."""
        self._description = description

    def set_quantity(self, quantity):
        """Set the quantity of the item."""
        self._quantity = quantity
        self._update_total_price()

    def set_unit_price(self, unit_price):
        """Set the unit price of the item."""
        self._unit_price = unit_price
        self._update_total_price()

    def _update_total_price(self):
        """Private method to update total price based on quantity and unit price."""
        self._total_price = self._quantity * self._unit_price

    def validate_item(self):
        """Validate the item details (e.g., ensure quantity and price are positive)."""
        if self._quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if self._unit_price < 0:
            raise ValueError("Unit price cannot be negative.")
        return True


def generate_delivery_note(customer, order, delivery, subtotal, taxes_and_fees, total_charges):
    """Generate and display a delivery note based on the provided objects."""
    print("Delivery Note")
    print("Thank you for using our delivery service! Please print your delivery receipt and present it upon receiving your items.\n")

    print("Recipient Details:")
    print(f"Name: {customer.get_name()}")
    print(f"Contact: {customer.get_email()}")
    print(f"Delivery Address: {customer.get_address()}\n")

    print("Delivery Information:")
    print(f"Order Number: {order.get_order_number()}")
    print(f"Reference Number: {order.get_reference_number()}")
    print(f"Delivery Date: {order.get_delivery_date()}")
    print(f"Delivery Method: {delivery.get_method()}")
    print(f"Package Dimensions: {delivery.get_weight()}\n")

    print("Summary of Items Delivered:")
    print("| Item Code | Description                 | Quantity | Unit Price (AED) | Total Price (AED) |")
    print("|-----------|-----------------------------|----------|------------------|-------------------|")
    for item in order.get_items():
        print(f"| {item.get_item_code()} | {item.get_description():<23} | {item.get_quantity()} | {item.get_unit_price():>14.2f} | {item.get_total_price():>15.2f} |")

    print(f"\nSubtotal: AED {subtotal:.2f}")
    print(f"Taxes and Fees: AED {taxes_and_fees:.2f}")
    print(f"Total Charges: AED {total_charges:.2f}")
