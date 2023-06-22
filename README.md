# Adapter (Structural)

Adapter pattern has both a class and object approach.

Adapter is useful when:
- You want to use an existing class, and its interface does not match the one you need.
- You want to create a reusable class that cooperates with unrelated or unforeseen classes (classes which may have incompatible interfaces).
-  [object adapter only] You need to use several existing subclasses an object adapter can adapt the interface of its parent class.

Clients call operations on an Adapter instance, and the Adapter calls the Adaptee operations that carry out the request. Two way adapters provide transparency. This is because an adapted object no longer conforms to the adaptee interface, so it can't be used as is wherever an adaptee object can.

**Benefits:**
Class Adapter:
- Lets Adapter override some of Adaptee's behavior since Adapter is a subclass of Adaptee.

Object Adapter:
- Lets a single Adapter work with many Adaptees (the Adaptee and all its subclasses)
- Adapter can add functionality to all Adaptees at once.

**Consequences:**
Class Adapter:
- Class adapter won't work when we want to adapt a class and all its subclasses.

Object Adapter:
- Makes it harder to override Adaptee behavior.
