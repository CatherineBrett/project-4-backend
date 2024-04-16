from app import app, db
from models.group import GroupModel
from models.category import CategoryModel
from models.group_category import GroupCategoryModel
from models.user import UserModel

with app.app_context():

    print("Creating the database...")
    db.drop_all()
    db.create_all()

    print("Seeding the database...")

    admin = UserModel(
    username="adminuser",
    email="admin@harbornecommunitygroups.com",
    password="P@ssword0!",
    )
    admin.save()

    catherine = UserModel(
        username="cbrett",
        email="cbrett@geemail.com",
        password="P@ssword1!",
    )
    catherine.save()

    wendy = UserModel(
        username="wjones",
        email="wjones@geemail.com",
        password="P@ssword2!",
    )
    wendy.save()

    harborne_walking_group = GroupModel(
        name="Harborne Walking Group",
        image="https://images.unsplash.com/photo-1580058572462-98e2c0e0e2f0?q=80&w=3542&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        brief_desc="We are Harborne Walking Group, and we meet every other Sunday for 5k walks in the local area.",
        contact_name="Diane",
        contact_number="07010 100 100",
        full_desc="Come and join our friendly walking group! Every other Sunday we meet on the high street and then do a 5k walk, finishing where we started. We often have refreshments at a cafe afterwards. All are welcome!",
        user_id=catherine.id,
    )
    harborne_walking_group.save()

    fitness = CategoryModel(name="Fitness")
    fitness.save()

    outdoors = CategoryModel(name="Outdoors")
    outdoors.save()

    hwg_fitness = GroupCategoryModel(
        group_id=harborne_walking_group.id, category_id=fitness.id
    )
    hwg_fitness.save()

    hwg_outdoors = GroupCategoryModel(
        group_id=harborne_walking_group.id, category_id=outdoors.id
    )
    hwg_outdoors.save()

    print("Database successfully seeded!")
