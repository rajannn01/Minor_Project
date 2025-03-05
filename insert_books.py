from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["book_recommendation"]

books = {
    "happy": [
        
        {"title": "The Return of Simple", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/080901582X.01.MZZZZZZZ.jpg
"},
        {"title": "The Forest House", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0451454243.01.MZZZZZZZ.jpg
"},
        {"title": "The Stars Shine Down", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0446364762.01.MZZZZZZZ.jpg
"},
        {"title": "The Secret Garden", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0812505018.01.MZZZZZZZ.jpg
"},  
        {"title": "Pride and Prejudice", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/055321215X.01.MZZZZZZZ.jpg
"},   
        {"title": "The Little Prince", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0156528207.01.MZZZZZZZ.jpg
"},
        {"title": "Harry Potter and the Sorcerer's Stone", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/059035342X.01.MZZZZZZZ.jpg
"},
        {"title": "The Hobbit", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0395177111.01.MZZZZZZZ.jpg
"},
        {"title": "The Bad Beginning (A Series of Unfortunate Events, Book 1)", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0064407667.01.MZZZZZZZ.jpg
"},
        {"title": "The Sorcerer's Companion: A Guide to the Magical World of Harry Potter", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0767908473.01.MZZZZZZZ.jpg
"},
        {"title": "Titan", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0425049981.01.MZZZZZZZ.jpg
"},
        {"title": "Sunwing", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0689832877.01.MZZZZZZZ.jpg
"},
        {"title": "Born of the Sun", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0453006663.01.MZZZZZZZ.jpg
"},
        {"title": "The White Puma", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/1558175326.01.MZZZZZZZ.jpg
"},
        {"title": "Enchantment", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0345416880.01.MZZZZZZZ.jpg
"},
        {"title": "The Hork-Bajir Chronicles (Animorphs Series)", "genre": "Fantasy", "image_url": "http://images.amazon.com/images/P/0439042917.01.MZZZZZZZ.jpg
"}, 
        {"title": "The Rescue", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/0446525502.01.MZZZZZZZ.jpg
"}, 
        {"title": "A Map of the World", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/0385500769.01.MZZZZZZZ.jpg
"},
        {"title": "Vinegar Hill", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/0688180639.01.MZZZZZZZ.jpg
"},
        {"title": "Angel Falls", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/0609605925.01.MZZZZZZZ.jpg
"},
        {"title": "The Saving Graces: A Novel ", "fictional": "Drama", "image_url": "https://images.amazon.com/images/P/0060191929.01.MZZZZZZZ.jpg
"},
        {"title": "The Vineyard: A Novel", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/0684864843.01.MZZZZZZZ.jpg
"},
        {"title": "The Looking Glass: A Novel", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/0684867818.01.MZZZZZZZ.jpg
"},
        {"title": "The Promise Remains", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/0684868911.01.MZZZZZZZ.jpg
"},
        {"title": "The Villa", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/052594463X.01.MZZZZZZZ.jpg
"},
        {"title": "In This Mountain", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/039304016X.01.MZZZZZZZ.jpg
"},
        {"title": "Blue Heaven", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/0140107649.01.MZZZZZZZ.jpg
"},
        {"title": "One Heart", "genre": "fictional", "image_url": "https://images.amazon.com/images/P/1570717257.01.MZZZZZZZ.jpg
"},
        {"title": "Anne of Green Gables", "genre": "Fiction", "image_url": "http://images.amazon.com/images/P/055321313X.01.MZZZZZZZ.jpg
"},     
        {"title": "The Big Bad Wolf", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/0553584588.01.MZZZZZZZ.jpg
"},

        {"title": "Four Blind Mice", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/1586214047.01.MZZZZZZZ.jpg
"},

        {"title": "Roses Are Red", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/1570429200.01.MZZZZZZZ.jpg
"},

        {"title": "Postmortem ", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/0671023616.01.MZZZZZZZ.jpg
"},

        {"title": "Body of Evidence", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/0671038567.01.MZZZZZZZ.jpg
"},

        {"title": "All That Remains", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/0765191121.01.MZZZZZZZ.jpg
"},

        {"title": "Relics (Star Trek: The Next Generation)", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/0671864769.01.MZZZZZZZ.jpg
"},

        {"title": "Blood Oath", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/0312953453.01.MZZZZZZZ.jpg
"},

        {"title": "Goodbye, My Little Ones: The True Story of a Murderous Mother and Five Innocent Victims", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/0451406923.01.MZZZZZZZ.jpg
"},

        {"title": "Coyote Waits (Joe Leaphorn/Jim Chee Novels)", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/0061099325.01.MZZZZZZZ.jpg
"},

        {"title": "The Cat Who Came to Breakfast (Cat Who... (Hardcover))", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/0399138684.01.MZZZZZZZ.jpg
"},
    {
        "title": "Citizens: A Chronicle of the French Revolution",
        "genre": "Historical Fiction",
        "image_url": "http://images.amazon.com/images/P/0679726101.01.MZZZZZZZ.jpg
"
    },
    
    {
        "title": "Stone Butch Blues",
        "genre": "Fiction",
        "image_url": "http://images.amazon.com/images/P/156341029X.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "Stardust",
        "genre": "Fiction",
        "image_url": "http://images.amazon.com/images/P/0060934719.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "The Beans of Egypt, Maine",
        "genre": "Fiction",
        "image_url": "http://images.amazon.com/images/P/0446300101.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "A Density of Souls",
        "genre": "Fiction",
        "image_url": "http://images.amazon.com/images/P/0786886463.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "Slow River",
        "genre": "Fiction",
        "image_url": "http://images.amazon.com/images/P/0345395379.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "The Space Merchants",
        "genre": "Science Fiction",
        "image_url": "http://images.amazon.com/images/P/0312749511.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "Dreamsnake",
        "genre": "Science Fiction",
        "image_url": "http://images.amazon.com/images/P/0395264707.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "Changer",
        "genre": "Science Fiction",
        "image_url": "http://images.amazon.com/images/P/0805062971.01.MZZZZZZZ.jpg"
    }
     {"title": "The Kite Runner", "genre": "Historical Fiction", "image_url": "http://images.amazon.com/images/P/1573222453.01.MZZZZZZZ.jpg
"},


]


        # Add 40 more real books
    ],
    "sad": [

    {"title": "Life’s Little Instruction Book", "genre": "Self-Help", "image_url": "http://images.amazon.com/images/P/0805062971.01.MZZZZZZZ.jpg
"},
    {"title": "Love, Medicine, and Miracles", "genre": "Self-Help", "image_url": "http://images.amazon.com/images/P/0060154969.01.MZZZZZZZ.jpg
"},
    {"title": "Getting Well Again", "genre": "Self-Help", "image_url": "http://images.amazon.com/images/P/0553259865.01.MZZZZZZZ.jpg
"},
    {"title": "The Therapeutic Touch", "genre": "Self-Help", "image_url": "http://images.amazon.com/images/P/067176537X.01.MZZZZZZZ.jpg
"},
    
    {"title": "Rich Dad, Poor Dad: What the Rich Teach Their Kids About Money--That the Poor and Middle Class Do Not!", "genre": "Self-Help", "image_url": "http://images.amazon.com/images/P/0446677450.01.MZZZZZZZ.jpg
"},
    {"title": "Creating Wealth: Retire in Ten Years Using Allen's Seven Principles of Wealth!", "genre": "Self-Help", "image_url": "http://images.amazon.com/images/P/0671621009.01.MZZZZZZZ.jpg
"},
    {"title": "Keep It Simple: And Get More Out of Life", "genre": "Self-Help", "image_url": "http://images.amazon.com/images/P/0002740230.01.MZZZZZZZ.jpg
"},
    {"title": "If Singleness Is a Gift, What's the Return Policy?", "genre": "Self-Help", "image_url": "http://images.amazon.com/images/P/0785263292.01.MZZZZZZZ.jpg
"},
    {"title": "Always Daddy's Girl: Understanding Your Father's Impact on Who You Are", "genre": "Self-Help", "image_url": "http://images.amazon.com/images/P/0830714014.01.MZZZZZZZ.jpg
"},
    {
    "title": "The 7 Habits of Highly Effective People",
    "genre": "Self-Help",
    "image_url": "http://images.amazon.com/images/P/1883219027.01.MZZZZZZZ.jpg
"
  },
  {
    "title": "Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones",
    "genre": "Self-Help",
    "image_url": "http://images.amazon.com/images/P/0735211299.01.MZZZZZZZ.jpg"
  },
  {
    "title": "The Power of Now: A Guide to Spiritual Enlightenment",
    "genre": "Self-Help",
    "image_url": "http://images.amazon.com/images/P/1577311523.01.MZZZZZZZ.jpg
"
  },
  {
    "title": "Self Analysis",
    "genre": "Self-Help",
    "image_url": "http://images.amazon.com/images/P/0884041093.01.MZZZZZZZ.jpg
"
  },
   {
    "title": "Come Before Winter and Share My Hope",
    "genre": "Self-Help",
    "image_url": "http://images.amazon.com/images/P/0842304770.01.MZZZZZZZ.jpg
"
  },
 {
        "title": "Fires of Aggar",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/1886383421.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "Return to Isis",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/0962893862.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "Twin Blessings",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/0373871562.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "Whisper to Me of Love",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/0380752115.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "Tender Triumph",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/0671614568.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "A Minor Indiscretion",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/0373250339.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "For Better, for Worse",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/0380820447.01.MZZZZZZZ.jpg

"
    },
      {
        "title": "Amanda Miranda ",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/0380538504.01.MZZZZZZZ.jpg

"
    },
      {
        "title": "Golden Cup",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/0440130913.01.MZZZZZZZ.jpg

"
    },
      {
        "title": "Hood",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/1555834531.01.MZZZZZZZ.jpg
"
    },
   
      {
        "title": "Boy Who Kicked Pigs ",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/1555834531.01.MZZZZZZZ.jpg
"
    },
      {
        "title": "Written on the Body ",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/067942007X.01.MZZZZZZZ.jpg
"
    },
      {
        "title": "Black Thorn, White Rose ",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/068813713X.01.MZZZZZZZ.jpg
"
   },
      {
        "title": "Fitcher's Brides ",
        "genre": "Romance",
        "image_url": "http://images.amazon.com/images/P/0765301954.01.MZZZZZZZ.jpg
"
    },

    {
        "title": "More George W. Bushisms",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/0743251008.01.MZZZZZZZ.jpg
"
    },

    {
        "title": "The World's Stupidest Laws",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/185479549X.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "The World's Stupidest Signs",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/1854795554.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "SO LONG AND THANKS FOR ALL THE FISH",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/0671745530.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "The Amazing Adventures of Kavalier & Clay",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/0312282990.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "The Real Mother Goose",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/0026890380.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "One Fish Two Fish Red Fish Blue Fish",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/0394800133.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "The Chocolate Korndog",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/074141127X.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "Eeyore's Little Book of Gloom",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/0416196772.01.MZZZZZZZ.jpg
"
    },
      {
        "title": "The Chocolate Korndog",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/074141127X.01.MZZZZZZZ.jpg

    },
       {
        "title": "Crazy from the Heat",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/0786889470.01.MZZZZZZZ.jpg
"
    },
       {
        "title": "Expecting Someone Taller",
        "genre": "Comedy",
        "image_url": "http://images.amazon.com/images/P/044122332X.01.MZZZZZZZ.jpg
"},

        {"title": "Moby-Dick", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0140390847.01.MZZZZZZZ.jpg
"},
        {"title": "Life of Pi", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0151008116.01.MZZZZZZZ.jpg
"},
        {"title": "The Call of the Wild", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0451527038.01.MZZZZZZZ.jpg
"},
        {"title": "The Phantom Tollbooth", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0394815009.01.MZZZZZZZ.jpg
"},
        {"title": "The Survivors Club", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0553584510.01.MZZZZZZZ.jpg
"},
        {"title": "Reap the Wind", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0553292447.01.MZZZZZZZ.jpg
"},
        {"title": "Jurassic Park", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0345370775.01.MZZZZZZZ.jpg
"}, 
        {"title": "Tracks ", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0060972459.01.MZZZZZZZ.jpg
"}, 
        {"title": "Daughter of Fortune", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/038082101X.01.MZZZZZZZ.jpg
"},  
        {"title": "Neverwhere", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0380973634.01.MZZZZZZZ.jpg

"},

        # Add 40 more real books
    ],
    "angry": [       
        
 {
        "title": "How Not to Say What You Mean: A Dictionary of Euphemisms",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0198604025.01.MZZZZZZZ.jpg
"
    },
   
    {
        "title": "College Majors and Careers: A Resource Guide for Effective Life Planning",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0894342789.01.MZZZZZZZ.jpg
"
    },
     {
        "title": "How to Win Friends and Influence People",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0671027034.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "The Grace and Truth Paradox: Responding with Christlike Balance",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/1590520653.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "Just Here Trying to Save a Few Lives",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0446677574.01.MZZZZZZZ.jpg


"
    },
    {
        "title": "So That Others May Live: Caroline Hebard & Her Search-And-Rescue Dogs",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0553574833.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "I Thought My Father Was God: And Other True Tales from NPR's National Story Project",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0312421001.01.MZZZZZZZ.jpg

"
    },
      {
        "title": "The Best Thing I Ever Did for My Marriage: 50 Real Life Stories",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/1590521994.01.MZZZZZZZ.jpg

"  },
  {
        "title": "Eat Smart, Think Smart",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0060170441.01.MZZZZZZZ.jpg


"
    },
      {
        "title": "Negaholics",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0712646221.01.MZZZZZZZ.jpg

"
    },
      {
        "title": "Third Eye",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0440987202.01.MZZZZZZZ.jpg


"
    },
      {
        "title": "Sympathy for the Devil",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0380795965.01.MZZZZZZZ.jpg


"
    },
      {
        "title": "Reviving Ophelia",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0345392825.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "Anam Cara",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0060182792.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "Seven Habits of Highly Effective People",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0671708635.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "Chicken Soup for the College Sou",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/1558747028.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "You're Fifty--Now What",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0609605623.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "Emotional Purity",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/1579213405.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "Feeling Good",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0688036333.01.MZZZZZZZ.jpg


"
    },
         {
        "title": "The Big Book of Calm",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0140282378.01.MZZZZZZZ.jpg


"
    },
         {
        "title": "What Women Want",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/037303752X.01.MZZZZZZZ.jpg



"
    },
         {
        "title": "The Self-Esteem Companion",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/1572241381.01.MZZZZZZZ.jpg


"
    },
         {
        "title": "Becoming a Critical Thinker",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0130289221.01.MZZZZZZZ.jpg


"
    },
         {
        "title": "How to Say It Style Guide",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/073520313X.01.MZZZZZZZ.jpg


"
    },
         {
        "title": "Just Here Trying to Save a Few Lives",
        "genre": "Motivational",
        "image_url": "http://images.amazon.com/images/P/0446677574.01.MZZZZZZZ.jpg


"
    },

 {
        "title": "Sofie's World: A Novel About the History of Philosophy",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/3423620005.01.MZZZZZZZ.jpg

"
    },

    {
        "title": "Common Phrases: And Where They Come From",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/1585746827.01.MZZZZZZZ.jpg

"
    },
    
    {
        "title": "Notions and Potions: A Safe, Practical Guide to Creating Magic & Miracles",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0806996021.01.MZZZZZZZ.jpg

"
    },
    
    {
        "title": "Entdecke den Schamanen in dir: Reise in die innere Welt des Alltags",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/3426871874.01.MZZZZZZZ.jpg

"
    },
    
    {
        "title": "Ishmael",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0671554271.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "The Complete I Ching –",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0553255959.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "El Poder Curativo de La Mente",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/8440691475.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "The Selfish Gene",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0192860925.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "Fahrenheit 451",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0345410017.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "1984",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0704339838.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "A Connecticut Yankee in King Arthur's Court",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0192839020.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "Skinny Legs and All",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0553377884.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "Sophie's Choice",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0553277499.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "Novecento",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/8874975554.01.MZZZZZZZ.jpg


"
    },
     {
        "title": "God-Shaped Hole",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/1570719586.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "Calliope's Sisters",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0131554255.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "Brave New World & Brave New World Revisited",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0060901012.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "The Book of the Dead",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/055327998X.01.MZZZZZZZ.jpg

"
    },
     {
        "title": "The Simple Truth",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/1570426384.01.MZZZZZZZ.jpg
"
    },
     {
        "title": "Schamanismus: Reisen der Seele, Magische Kräfte, Ekstase und Heilung",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/3822813397.01.MZZZZZZZ.jpg

"
    }, 
      {
        "title": "Man's Search for Meaning",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0671023373.01.MZZZZZZZ.jpg
"
    },
      {
        "title": "The Evolution of Desire",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0465077501.01.MZZZZZZZ.jpg

"
    },
      {
        "title": "A Walk in the Woods",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0553455923.01.MZZZZZZZ.jpg
"
    },
      {
        "title": "Northanger Abbey",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/3829030010.01.MZZZZZZZ.jpg
"
    },
      {
        "title": "Nostromo",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/0486424529.01.MZZZZZZZ.jpg
"
    },
      {
        "title": "Othello",
        "genre": "Philosophical",
        "image_url": "http://images.amazon.com/images/P/1853260185.01.MZZZZZZZ.jpg
"
    },
       {
        "title": "The Little Book of Big Ideas: Inspiration, Encouragement &amp",
        "genre": "Spiritual",
        "image_url": "http://images.amazon.com/images/P/1581820542.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "The Celestine Prophecy",
        "genre": "Spiritual",
        "image_url": "http://images.amazon.com/images/P/1570422826.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "A Big New Free Happy Unusual Life",
        "genre": "Spiritual",
        "image_url": "http://images.amazon.com/images/P/0767910079.01.MZZZZZZZ.jpg
"
    },
    {
        "title": "Celtic Mythology",
        "genre": "Spiritual",
        "image_url": "http://images.amazon.com/images/P/087226002X.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "Ancient Celtic",
        "genre": "Spiritual",
        "image_url": "http://images.amazon.com/images/P/1855853906.01.MZZZZZZZ.jpg

"
    },
    {
        "title": "The Western Way",
        "genre": "Spiritual",
        "image_url": "http://images.amazon.com/images/P/1850630127.01.MZZZZZZZ.jpg
"
    },
  

        
    ],
    "surprise": [
        {"title": "Gone Girl", "genre": "Thriller", "image_url": "https://example.com/gone_girl.jpg"},
        {"title": "The Girl on the Train", "genre": "Mystery", "image_url": "https://example.com/the_girl_on_the_train.jpg"},
        {"title": "The Da Vinci Code", "genre": "Mystery", "image_url": "http://images.amazon.com/images/P/0385504209.01.MZZZZZZZ.jpg
"},
        {"title": "Shutter Island", "genre": "Thriller", "image_url": "http://images.amazon.com/images/P/038073186X.01.MZZZZZZZ.jpg
"},
        {"title": "The Silent Patient", "genre": "Psychological Thriller", "image_url": "https://example.com/the_silent_patient.jpg"},
        {"title": "Before I Go to Sleep", "genre": "Psychological Thriller", "image_url": "https://example.com/before_i_go_to_sleep.jpg"},
        {"title": "Big Little Lies", "genre": "Mystery", "image_url": "https://example.com/big_little_lies.jpg"},
        {"title": "The Couple Next Door", "genre": "Thriller", "image_url": "https://example.com/the_couple_next_door.jpg"},
        {"title": "The Woman in the Window", "genre": "Psychological Thriller", "image_url": "https://example.com/the_woman_in_the_window.jpg"},
        {"title": "The Girl with the Dragon Tattoo", "genre": "Mystery", "image_url": "https://example.com/the_girl_with_the_dragon_tattoo.jpg"},
        # Add 40 more real books
    ],
    "cool": [
        {"title": "To Kill a Mockingbird", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0446310786.01.MZZZZZZZ.jpg
"},
        {"title": "Moby-Dick", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0140390847.01.MZZZZZZZ.jpg
"},
        {"title": "Life of Pi", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0151008116.01.MZZZZZZZ.jpg
"},
        {"title": "The Call of the Wild", "genre": "Adventure", "image_url": "http://images.amazon.com/images/P/0451527038.01.MZZZZZZZ.jpg
"},
        {"title": "Into the Wild", "genre": "Biography", "image_url": "http://images.amazon.com/images/P/0385486804.01.MZZZZZZZ.jpg
"},
        {"title": "The Old Man and the Sea", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0020519109.01.MZZZZZZZ.jpg
"},
        {"title": "The Alchemist", "genre": "Philosophical Fiction", "image_url": "http://images.amazon.com/images/P/0062502174.01.MZZZZZZZ.jpg
"},
        {"title": "Siddhartha", "genre": "Philosophical Fiction", "image_url": "http://images.amazon.com/images/P/0553208845.01.MZZZZZZZ.jpg
"},
        {"title": "Walden", "genre": "Philosophy", "image_url": "http://images.amazon.com/images/P/055321246X.01.MZZZZZZZ.jpg
"},
        {"title": "Zen and the Art of Motorcycle Maintenance", "genre": "Philosophical Fiction", "image_url": "http://images.amazon.com/images/P/0553277472.01.MZZZZZZZ.jpg
"},
        {"title": "To Kill a Mockingbird", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0020519109.01.MZZZZZZZ.jpg"},
      { "title": "Pride and Prejudice", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0020519109.01.MZZZZZZZ.jpg   "}
       {"title": "Heart of Darkness", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0020519109.01.MZZZZZZZ.jpg"}
      {"title": "Black Beauty", "genre": "Classic", "image_url": "http://images.amazon.com/images/P/0020519109.01.MZZZZZZZ.jpg"}
        # Add 40 more real books
    ]
}

# Insert books into the database
for emotion, book_list in books.items():
    collection = db[emotion]
    collection.insert_many(book_list)

print("50 books for each emotion have been inserted successfully!")