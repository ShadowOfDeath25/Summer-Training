class Cars:
    manu = ""
    model = ""
    year = ""
    id = ""
    owner_id = ""
    engine_capacity = 0
    horsepower = 0
    top_speed = 0
    price = 0
    photo_path = ""
    description = ""
    op_type = ""
    state = ""
    owner_phone= ""

    def __init__(self, manu, model, year, ID, owner_id, engine_capacity, horsepower, top_speed, price, photo_path,
                 description, op_type, state,owner_phone):
        self.manu = manu
        self.model = model
        self.year = year
        self.id = ID
        self.owner_id = owner_id
        self.engine_capacity = engine_capacity
        self.horsepower = horsepower
        self.top_speed = top_speed
        self.price = price
        self.photo_path = photo_path
        self.description = description
        self.op_type = op_type
        self.state = state
        self.owner_phone=owner_phone

