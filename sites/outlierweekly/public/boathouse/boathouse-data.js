// Boathouse Riverside menu dataset.
// Source: kitchen service and plating cards (44 plated items), photographed 2026-11-11.
// Dietary flags are INFERRED from the written ingredient builds, not printed on the cards.
// dairy / gluten / veg / vegan are booleans. "note" explains anything a server must confirm.

window.BOATHOUSE_ITEMS = [
  // ---------- SOUPS & SALADS ----------
  {
    name: "Crab & Corn Chowder",
    section: "Soups & Salads",
    ing: "Sweet crab, roasted corn, potatoes, herbs and creamy chowder broth",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Creamy chowder carries dairy; a flour-thickened chowder carries gluten. Shellfish present."
  },
  {
    name: "Gazpacho of the Day",
    section: "Soups & Salads",
    ing: "Chef's fall selection of local produce in a chilled seasonal soup",
    dairy: false, gluten: false, veg: true, vegan: true,
    note: "Produce-only build. Confirm the day's garnish and that no bread thickener was used."
  },
  {
    name: "Autumn Burrata Salad",
    section: "Soups & Salads",
    ing: "Burrata, autumn greens, agrodolce Gala apples, squash, cranberries, pepitas and white balsamic",
    dairy: true, gluten: false, veg: true, vegan: false,
    note: "Burrata is fresh cow's milk cheese. No grain in the build."
  },
  {
    name: "Chef's Vibrant Beet Salad",
    section: "Soups & Salads",
    ing: "Red and gold beets, Brussels sprouts, baby greens, goat cheese, pecans, couscous, clementine and white balsamic",
    dairy: true, gluten: true, veg: true, vegan: false,
    note: "Goat cheese is dairy. Couscous is wheat, so the salad is not gluten-free."
  },
  {
    name: "Grilled Steak Salad",
    section: "Soups & Salads",
    ing: "Grilled steak, baby greens, arugula, tomato, red onion, cucumber, blue cheese and mustard vinaigrette",
    dairy: true, gluten: false, veg: false, vegan: false,
    note: "Blue cheese is dairy. Mustard vinaigrette is normally gluten-free; confirm the mustard brand."
  },
  {
    name: "Dockside Wedge Salad",
    section: "Soups & Salads",
    ing: "Iceberg wedge, tomatoes, bacon, egg, blue cheese, ranch and balsamic glaze",
    dairy: true, gluten: false, veg: false, vegan: false,
    note: "Blue cheese and ranch are dairy. Bacon and egg make it non-vegetarian."
  },
  {
    name: "Caesar Salad",
    section: "Soups & Salads",
    ing: "Romaine, parmesan, garlic croutons and house Caesar dressing",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Parmesan is dairy, croutons are wheat. Classic Caesar dressing also carries anchovy and egg."
  },
  {
    name: "Greek Salad",
    section: "Soups & Salads",
    ing: "Baby greens, tomato, onion, cucumber, peppers, olives, feta and red wine vinaigrette",
    dairy: true, gluten: false, veg: true, vegan: false,
    note: "Feta is dairy. Everything else in the build is produce and oil."
  },

  // ---------- HAND HELDS ----------
  {
    name: "Bacon Barge Smashburger",
    section: "Hand Helds",
    ing: "7 oz steak burger, cheddar, cola-chipotle bacon jam, crispy shallots and arugula",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Cheddar is dairy, the bun carries gluten and wheat. Bacon jam is pork."
  },
  {
    name: "The Catamaran Chicken Sandwich",
    section: "Hand Helds",
    ing: "Chicken breast, house slaw, Rude Booy sauce, lettuce and pickles on a challah bun",
    dairy: false, gluten: true, veg: false, vegan: false,
    note: "Challah bun is wheat and egg. Slaw dressing is mayonnaise-based, which is egg, not dairy."
  },
  {
    name: "Chicken Pesto Panini",
    section: "Hand Helds",
    ing: "Grilled chicken, basil pesto, roasted tomatoes and mozzarella on a pressed hoagie roll",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Mozzarella and pesto parmesan are dairy. Pesto also carries pine nuts. Roll is wheat."
  },
  {
    name: "Chicken Caesar Salad Wrap",
    section: "Hand Helds",
    ing: "Seasoned chicken, romaine, Caesar dressing, anchovy paste and garlic croutons in a flour tortilla",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Flour tortilla and croutons are wheat. Dressing carries parmesan plus anchovy and egg."
  },
  {
    name: "Garden Veggie Wrap",
    section: "Hand Helds",
    ing: "Hummus, roasted eggplant, peppers and tomatoes, mixed greens, herb vinaigrette and avocado in a spinach tortilla",
    dairy: false, gluten: true, veg: true, vegan: true,
    note: "The plant-based build on the menu. Spinach tortilla is still wheat, so it is vegan but not gluten-free."
  },
  {
    name: "Fried Tackle Box Fish Tacos",
    section: "Hand Helds",
    ing: "Popcorn-fried fish, tortillas, arugula, pickled onion, green Tabasco aioli, pico and chips, finished with cilantro",
    dairy: false, gluten: true, veg: false, vegan: false,
    note: "Batter and tortillas are wheat. Green Tabasco aioli is mayonnaise-based, so egg not dairy."
  },
  {
    name: "Pressed Cuban Panini",
    section: "Hand Helds",
    ing: "Mojo pork, Black Forest ham, Swiss, pickles and Dijonnaise on a pressed hoagie roll",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Swiss is dairy. Dijonnaise is egg-based. Pork and ham make it non-vegetarian."
  },
  {
    name: "Boathouse Crab Cakes",
    section: "Hand Helds",
    ing: "Three one-ounce crab cakes with remoulade, charred lemon and vegetable brunoise",
    dairy: false, gluten: true, veg: false, vegan: false,
    note: "Crab is shellfish, remoulade is egg-based. Cake binder and breadcrumb carry wheat."
  },

  // ---------- STARTERS ----------
  {
    name: "Bang Bang Brussels Sprouts",
    section: "Starters",
    ing: "Crisp Brussels sprouts, honey-gochujang glaze, bang bang sauce, scallions and sesame",
    dairy: false, gluten: true, veg: true, vegan: false,
    note: "Honey and egg-based bang bang sauce make it vegetarian but not vegan. Gochujang often contains wheat."
  },
  {
    name: "Boathouse Wings",
    section: "Starters",
    ing: "Crisp wings with ranch, celery and a choice of Korean BBQ, Buffalo or bourbon-whiskey glaze",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Ranch is dairy. Korean BBQ and bourbon glazes normally carry soy sauce, which is wheat."
  },
  {
    name: "Fried Coconut Shrimp",
    section: "Starters",
    ing: "Golden coconut shrimp with house-made mango-habanero dipping sauce",
    dairy: false, gluten: true, veg: false, vegan: false,
    note: "Coconut crust and fryer batter carry wheat. Shellfish present. Coconut is a tree nut for labeling."
  },
  {
    name: "Sautéed Shrimp",
    section: "Starters",
    ing: "Shrimp sautéed with butter, white wine, garlic, herbs, basil and paprika, served with toasted baguette",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Butter is dairy and the baguette is wheat. The pan sauce also contains white wine."
  },
  {
    name: "Loaded Potato Dippers",
    section: "Starters",
    ing: "Crisp potato dippers with sharp cheddar sauce, bacon and scallions",
    dairy: true, gluten: false, veg: false, vegan: false,
    note: "Cheddar sauce is dairy. Bacon makes it non-vegetarian. Potatoes alone carry no gluten."
  },
  {
    name: "Steamed Mussels Moqueca",
    section: "Starters",
    ing: "Mussels with tomato, palm oil, coconut broth, red onion, peppers and toasted baguette",
    dairy: false, gluten: true, veg: false, vegan: false,
    note: "The broth is coconut-based, not cream. The toasted baguette is the only gluten on the plate."
  },
  {
    name: "Smoked Fish Dip",
    section: "Starters",
    ing: "Smoked fish dip with fire-roasted peppers, pickles, house-made potato chips, made with mayonnaise, cream cheese and sour cream",
    dairy: true, gluten: false, veg: false, vegan: false,
    note: "Cream cheese and sour cream are dairy. Potato chips carry no gluten; confirm if crackers are added."
  },
  {
    name: "Greek Mezze Dip Platter",
    section: "Starters",
    ing: "Hummus, spicy feta, dill-mint tzatziki, vegetables, olives, tapenade and pita bites",
    dairy: true, gluten: true, veg: true, vegan: false,
    note: "Feta and tzatziki are dairy. Pita is wheat. Hummus and tahini carry sesame."
  },
  {
    name: "Guacamole",
    section: "Starters",
    ing: "Hand-pressed avocado, jalapeño, red onion, cilantro, tomato and lime with tortilla chips",
    dairy: false, gluten: false, veg: true, vegan: true,
    note: "Fully plant-based, and the corn tortilla chips are gluten-free."
  },
  {
    name: "Smoky Street Corn Dip with Queso Fresco",
    section: "Starters",
    ing: "Fire-roasted corn, micro cilantro, lime aioli, Tajín and queso fresco with house-fried corn chips",
    dairy: true, gluten: false, veg: true, vegan: false,
    note: "Queso fresco is dairy. Corn chips are gluten-free. Lime aioli is egg-based."
  },
  {
    name: "Toasted Tuna Poke Platter",
    section: "Starters",
    ing: "Citrus-ponzu ahi tuna, avocado, cucumber, yuzu, bang bang avocado crema, wasabi aioli and crisp wontons",
    dairy: false, gluten: true, veg: false, vegan: false,
    note: "Wontons are wheat and ponzu carries soy. Crema and aioli are egg-based, not dairy."
  },
  {
    name: "Grilled Swordfish Escabeche",
    section: "Starters",
    ing: "Adobo-grilled swordfish, hot-pickled vegetables, olives, citrus butter, avocado, crema and yuca fries",
    dairy: true, gluten: false, veg: false, vegan: false,
    note: "Citrus butter and crema are dairy. Yuca fries carry no gluten."
  },

  // ---------- FLATBREADS ----------
  {
    name: "Tomato + Basil Flatbread",
    section: "Flatbreads",
    ing: "House pizza sauce, mozzarella, tomatoes and basil on rosemary-infused flatbread",
    dairy: true, gluten: true, veg: true, vegan: false,
    note: "Mozzarella is dairy and the flatbread is wheat. Vegetarian as built."
  },
  {
    name: "Rustic Pepperoni Flatbread",
    section: "Flatbreads",
    ing: "House pizza sauce, pepperoni, mozzarella, roasted tomato and olive oil on rosemary flatbread",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Mozzarella is dairy, pepperoni is meat, flatbread is wheat."
  },
  {
    name: "Exotic Mushroom + Arugula Flatbread",
    section: "Flatbreads",
    ing: "Mushroom duxelles, arugula, balsamic glaze, oven-roasted tomato and goat cheese cream on rosemary flatbread",
    dairy: true, gluten: true, veg: true, vegan: false,
    note: "Goat cheese cream is dairy, flatbread is wheat. Vegetarian as built."
  },
  {
    name: "Whitehaven Seafood Flatbread",
    section: "Flatbreads",
    ing: "Seasoned seafood, olives, peppadew tapenade, capers, broccoli rabe and mozzarella",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Mozzarella is dairy, flatbread is wheat. Carries shellfish and fish."
  },

  // ---------- SEA SIDE ENTREES ----------
  {
    name: "Honey Sriracha Salmon",
    section: "Sea Side Entrees",
    ing: "Glazed salmon with bok choy, mushrooms, peppers, onion, carrots and steamed white rice",
    dairy: false, gluten: true, veg: false, vegan: false,
    note: "No dairy on the plate. Sriracha and glaze normally carry soy sauce, which is wheat."
  },
  {
    name: "Crispy Seared Branzino",
    section: "Sea Side Entrees",
    ing: "Mediterranean sea bass, golden beet-saffron risotto, beet coulis, charred lemon and herbs",
    dairy: true, gluten: false, veg: false, vegan: false,
    note: "Risotto is finished with butter and cheese. No wheat in the build."
  },
  {
    name: "Blackened Redfish + Grits",
    section: "Sea Side Entrees",
    ing: "Florida red drum, stone-ground corn grits and Florida corn-tomato chow chow",
    dairy: true, gluten: false, veg: false, vegan: false,
    note: "Grits are cooked with dairy. Corn grits carry no gluten."
  },
  {
    name: "Shrimp Scampi Pasta",
    section: "Sea Side Entrees",
    ing: "Sautéed shrimp, white wine, butter, garlic, lemon, tomato and basil with linguini",
    dairy: true, gluten: true, veg: false, vegan: false,
    note: "Butter is dairy and linguini is wheat. Pan sauce contains white wine."
  },

  // ---------- LAND LOVERS ----------
  {
    name: "Bistro Grilled NY Strip",
    section: "Land Lovers",
    ing: "10 oz NY strip, steakhouse frites, peppercorn sauce and baby gem salad",
    dairy: true, gluten: false, veg: false, vegan: false,
    note: "Peppercorn sauce is finished with butter and cream. Steak, frites and salad carry no gluten."
  },
  {
    name: "Caribbean Jerk Half Chicken",
    section: "Land Lovers",
    ing: "Jerk-marinated half chicken, corn festival cakes, honey-jerk glaze and mango relish",
    dairy: false, gluten: true, veg: false, vegan: false,
    note: "Corn festival cakes are fried dough, so gluten. No dairy in the build."
  },
  {
    name: "Calabrian Chili Honey Glazed Pork Chop",
    section: "Land Lovers",
    ing: "12 oz NC Duroc chop, broccoli rabe, cannellini beans, chili-honey glaze and apple agrodolce",
    dairy: false, gluten: false, veg: false, vegan: false,
    note: "No dairy and no wheat in the build. Honey glaze keeps it from being vegan."
  },

  // ---------- BOWLS ----------
  {
    name: "Umami Vegetable Stir-Fried Rice",
    section: "Bowls",
    ing: "White rice, bok choy, cabbage, cauliflower, peppers and aromatics in house umami sauce",
    dairy: false, gluten: true, veg: true, vegan: false,
    note: "No dairy. Soy-based umami sauce carries wheat. Confirm whether the sauce is fish-free before calling it vegan."
  },

  // ---------- SWEET TREATS ----------
  {
    name: "Mac + Cheese",
    section: "Sweet Treats",
    ing: "Orecchiette in sharp cheddar sauce with a cheesy, crispy garlic crust",
    dairy: true, gluten: true, veg: true, vegan: false,
    note: "Cheddar sauce and crust are dairy. Orecchiette is wheat."
  },
  {
    name: "5-Layer Chocolate Indulgence Cake",
    section: "Sweet Treats",
    ing: "Dark chocolate cake, raspberry caviar, whipped cream and wild berries",
    dairy: true, gluten: true, veg: true, vegan: false,
    note: "Whipped cream is dairy and the sponge is wheat. Vegetarian as built."
  },
  {
    name: "Key Lime Pie",
    section: "Sweet Treats",
    ing: "Key lime pie with whipped cream and fresh berries",
    dairy: true, gluten: true, veg: true, vegan: false,
    note: "Whipped cream and the filling carry dairy. The crumb crust is wheat."
  },
  {
    name: "Pineapple Upside-Down Cake",
    section: "Sweet Treats",
    ing: "Glazed pineapple rings, brown-butter sponge cake and piña colada cream",
    dairy: true, gluten: true, veg: true, vegan: false,
    note: "Brown butter and cream are dairy. Sponge cake is wheat."
  }
];
