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

    # TO-DO: Put these in a list??

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

    george = UserModel(
        username="gsmith",
        email="gsmith@geemail.com",
        password="P@ssword3!",
    )
    george.save()

    # TO_DO: Put these in a list??

    harborne_walking_group = GroupModel(
        name="Harborne Walking Group",
        image="https://images.unsplash.com/photo-1580058572462-98e2c0e0e2f0?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8d2Fsa2luZyUyMGdyb3VwfGVufDB8MHwwfHx8Mg",
        brief_desc="Easy-going walking group.",
        contact_name="Catherine",
        contact_number="07010 110 110",
        full_desc="Come and join our friendly walking group! Every other Sunday we meet on the high street and then do a 5k walk, finishing where we started. We often have refreshments at a cafe afterwards. All are welcome!",
        user_id=catherine.id,
    )
    harborne_walking_group.save()

    nifty_knitters = GroupModel(
        name="Nifty Knitters",
        image="https://images.unsplash.com/photo-1562469162-c17fc5155156?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8a25pdHRpbmd8ZW58MHwwfDB8fHwy",
        brief_desc="Knitting group for all ages!",
        contact_name="Wendy",
        contact_number="07020 220 220",
        full_desc="We meet once a week on a Wednesday evening for some company while we work on our individual creations, and also help each other out along the way! Call Wendy for more info.",
        user_id=wendy.id,
    )
    nifty_knitters.save()

    harborne_daytrippers = GroupModel(
        name="Harborne Daytrippers",
        image="https://images.unsplash.com/photo-1557223562-6c77ef16210f?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8YnVzJTIwdG91ciUyMGZyZWUlMjB0byUyMHVzZXxlbnwwfDB8MHx8fDI",
        brief_desc="Days out in the Midlands amongst friends!",
        contact_name="George",
        contact_number="07030 330 330",
        full_desc="At Harborne Daytrippers we take it in turns to organise a day out to a Midlands attraction on the last Saturday of each month. We try to keep the cost of tickets and transport down to under £50. We look forward to meeting you!",
        user_id=george.id,
    )
    harborne_daytrippers.save()

    birmingham_bookworms = GroupModel(
        name="Birmingham Bookworms",
        image="https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGJvb2slMjBncm91cCUyMGZyZWUlMjB0byUyMHVzZXxlbnwwfDB8MHx8fDI",
        brief_desc="Friendly reading group.",
        contact_name="Catherine",
        contact_number="07010 110 110",
        full_desc="Our friendly reading group meets once a month on a Monday evening to discuss our latest book. Feel free to come along every month, or to skip a month if you don't fancy the book we've chosen! Call Catherine for more info!",
        user_id=catherine.id,
    )
    birmingham_bookworms.save()

    italian_conversation = GroupModel(
        name="Italian Conversation Group",
        image="https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cm9tZSUyMGZyZWUlMjB0byUyMHVzZXxlbnwwfDB8MHx8fDI",
        brief_desc="Join other learners of Italian for conversation practice.",
        contact_name="Wendy",
        contact_number="07020 220 220",
        full_desc="Every other Thursday we meet to practise our Italian. We members at all levels, from beginner to advanced - all are welcome at our supportive group.",
        user_id=wendy.id,
    )
    italian_conversation.save()

    golden_gardeners = GroupModel(
        name="The Golden Gardeners",
        image="https://images.unsplash.com/photo-1584479898061-15742e14f50d?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGdhcmRlbmluZyUyMGZyZWUlMjB0byUyMHVzZXxlbnwwfDB8MHx8fDI",
        brief_desc="Enthusiastic gardening group!",
        contact_name="George",
        contact_number="07030 330 330",
        full_desc="At Golden Gardeners we help each other to look after our gardens. As the saying goes, many hands make light work. And there's plenty of time for tea cake, too!",
        user_id=george.id,
    )
    golden_gardeners.save()

    drama_queens = GroupModel(
        name="The Drama Queens",
        image="https://images.unsplash.com/photo-1516307365426-bea591f05011?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8dGhlYXRyZSUyMGZyZWUlMjB0byUyMHVzZXxlbnwwfDB8MHx8fDI",
        brief_desc="A local group of theatregoers.",
        contact_name="Catherine",
        contact_number="07010 110 110",
        full_desc="The Drama Queens organise theatre trips to the city centre, and sometimes further afield if there's something great on! Join us as little or as often as you'd like.",
        user_id=catherine.id,
    )
    drama_queens.save()

    harborne_social_group = GroupModel(
        name="Harborne Social Group",
        image="https://images.unsplash.com/photo-1606509036992-4399d5c5afe4?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y29mZmVlJTIwY3Vwc3xlbnwwfDB8MHx8fDI",
        brief_desc="Informal social group.",
        contact_name="Wendy",
        contact_number="07020 220 220",
        full_desc="We are a (very!) informal social group and we meet on the first Sunday of every month for coffee and/or brunch on the high street. We have members of all ages. Give Wendy a call if you'd like to come along!",
        user_id=wendy.id,
    )
    harborne_social_group.save()

    categories = [
        CategoryModel(name="Arts & Crafts"),
        CategoryModel(name="Culture"),
        CategoryModel(name="Education"),
        CategoryModel(name="Excursions"),
        CategoryModel(name="Fitness"),
        CategoryModel(name="Outdoors"),
        CategoryModel(name="Reading"),
        CategoryModel(name="Social"),
    ]
    for category in categories:
        category.save()

    # TO-DO: Figure out how to do this without hardcoding the IDs. And preferably put them in a list:

    hwg_fitness = GroupCategoryModel(group_id=harborne_walking_group.id, category_id=5)
    hwg_fitness.save()

    hwg_outdoors = GroupCategoryModel(group_id=harborne_walking_group.id, category_id=6)
    hwg_outdoors.save()

    knitters_crafts = GroupCategoryModel(group_id=nifty_knitters.id, category_id=1)
    knitters_crafts.save()

    daytrippers_culture = GroupCategoryModel(
        group_id=harborne_daytrippers.id, category_id=2
    )
    daytrippers_culture.save()

    daytrippers_excursions = GroupCategoryModel(
        group_id=harborne_daytrippers.id, category_id=4
    )
    daytrippers_excursions.save()

    daytrippers_social = GroupCategoryModel(
        group_id=harborne_daytrippers.id, category_id=8
    )
    daytrippers_social.save()

    bookworms_culture = GroupCategoryModel(
        group_id=birmingham_bookworms.id, category_id=2
    )
    bookworms_culture.save()

    bookworms_reading = GroupCategoryModel(
        group_id=birmingham_bookworms.id, category_id=7
    )
    bookworms_reading.save()

    italian_culture = GroupCategoryModel(
        group_id=italian_conversation.id, category_id=2
    )
    italian_culture.save()

    italian_education = GroupCategoryModel(
        group_id=italian_conversation.id, category_id=3
    )
    italian_education.save()

    italian_social = GroupCategoryModel(group_id=italian_conversation.id, category_id=8)
    italian_social.save()

    gardeners_outdoors = GroupCategoryModel(group_id=golden_gardeners.id, category_id=6)
    gardeners_outdoors.save()

    drama_queens_culture = GroupCategoryModel(group_id=drama_queens.id, category_id=2)
    drama_queens_culture.save()

    drama_queens_excursions = GroupCategoryModel(
        group_id=drama_queens.id, category_id=4
    )
    drama_queens_excursions.save()

    drama_queens_social = GroupCategoryModel(group_id=drama_queens.id, category_id=8)
    drama_queens_social.save()

    social_group_social = GroupCategoryModel(
        group_id=harborne_social_group.id, category_id=8
    )
    social_group_social.save()

    print("Database successfully seeded!")
