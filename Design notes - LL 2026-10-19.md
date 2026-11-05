Design notes 2026-10-19



2026-10-07  Initial design thoughts - Production Planning module.

- Primary Problem: JSON vs Database? 
    - JSON is easier to read and write, but lacks the ability to store complex data structures
    - Database is excellent for scalability however it requires more effort to manage and scale. It is also something new to learn.
    - Database is the obvious choice for a Brewery production system. HOWEVER - the scale and scope of the a *beginners coding project* is too small to justify the effort required to learn and implement a database.
    - JSON is the chosen method of choice for this project, it is lightweight, approachable, and can incorporate OOP concepts in an approachable manner, however, during disucssion, it should be mentioned that should this be scaled and rolled out for an actual use, a database would be the preferred choice. 


- Four JSON files: products, materials, recipes, work_orders
    - products: What do we make? 
    - materials: What do we use? 
    - recipes: How do we make it? 
    - work_orders: What do we do? 

- Work_order >> Product >> Recipe >> Materials

- Products and materials are linked by ID
    - This makes linking across JSONs easier
- Recipes store amount per ONE unit
    - This gives good scabaility and context, we will also include the unit as a property. 
- Link by ID only; recipes store amount per ONE unit
    - This ensures consistency across all recipes and validates by immutable value incase of slight renames
- Material requirements calculated on demand, not stored. General coding principle researched "never store what you can calculate". 

- Planning unit owns work_orders.json, other units may need access but should not be able to modify properties, the only exception to this will be admin users or certain users being able to update order status. 



2026-10-20  further Design thoughts - Planning module

- Basic UI thoughts - CLI terminal interaction with ASCII art for logo 
- 


2026-10-21 - JSON // OOP thoughts

- JSON represents permanent record, objects represent the data inside memory
- Reading into objects can constitute the intialisation function? 
- when to save? big question
- JSON load and save functions should sit in thier own file so other modules can import, this will be needed across all 

- Reading into classes and data classes 
    - Classes need a __init__ function to initialise the object
    - Lots of manual self.ID, self.product etc etc 
    - Dataclasses skip this and just use type hinting to construct the class ID: str, productL str, (**data) etc
    - Dataclasses are great for simple objects, but for complex objects, they can be difficult to read and write
    - Data classes would be used for this project until it came time for data validation and error handling. That is where PyDantic data models can excel. 
    - Pydantic data models are great for validating and error handling data, they come with built-in validators and error messages. They are also useful as they contain out the box functions to serialise and deserialise the data back into the JSON format. 
    - Errors are found at runtime and not halfway through the code, which is why they are important to have in place. Pydantic will check data types against the type hinting and raise bespoke errors if the data does not match the type hinting.
    - For this reason, the project continues forward with Pydantic data models for OOP aspects.

- For the purpose of the project and design decisions I will write a WorkOrder class in all 3 forms, a conventional class, a dataclass, and a pydantic model. This is to illustrate the differences between these three forms of data modelling.

