import media
import fresh_tomatoes


'''
The entertainment center holds all movie titles in the following format:

media.Movie(	"Title",
	"Plot",
	"Poster",
	"Trailer")


NOTE: While the functionality for the plot has yet to be implemented,
 all plot information below comes from Wikipedia.

##Source: https://en.wikipedia.org/wiki/List_of_Pixar_films

Clicking on each image will open a trailer for that movie.

'''

toy_story = media.Movie(	"Toy Story",
	"""In a world where toys are living things who pretend to be lifeless when
	 humans are present, a group of toys, owned by six-year-old Andy Davis,
	 are caught off-guard when Andy's birthday party is moved up a week,
	 as Andy, his mother, and infant sister Molly, are preparing to move
	 the following week. The toys' leader and Andy's favorite toy,
	 a pull-string cowboy doll named Sheriff Woody, organizes the other toys,
	 including Bo Peep the shepherdess, Mr. Potato Head, Rex the Dinosaur,
	 Hamm the Piggy Bank, and Slinky Dog, into a scouting mission.
	 Green army men, led by Sarge, spy on the party, and report the results
	 to the others via baby monitors. The toys are relieved when the party
	 appears to end with none of them having been replaced, but then Andy
	 receives a surprise gift - an electronic toy space ranger action figure
	 named Buzz Lightyear, who thinks he is an actual space ranger.""",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

a_bugs_life = media.Movie(	"A Bug's Life",
	"""Ant Island is a colony of ants led by the Queen and her daughter,
	 Princess Atta. Every season, they are forced to give food to a gang
	 of marauding grasshoppers led by Hopper. One day, when Flik,
	 an individualist and would-be inventor, inadvertently knocks the
	 offering into a stream with his latest invention,
	 a grain harvesting device, Hopper demands twice as much food as
	 compensation. When Flik suggests in earnest that they seek help from
	 other stronger bugs, the other ants see it as an opportunity to remove
	 him and send him off.""",
	"https://upload.wikimedia.org/wikipedia/en/c/cc/A_Bug%27s_Life.jpg",
	"https://www.youtube.com/watch?v=Ljk2YJ53_WI")

toy_story_2 = media.Movie(	"Toy Story 2",
	"""Andy prepares to go to cowboy camp with Woody, but while playing with
	 Woody and Buzz, he accidentally tears Woody's arm. Andy's mom puts Woody
	 on a shelf, and Andy leaves without Woody. The next day, Woody finds
	 that Wheezy has been shelved for months due to a broken squeaker. Andy's
	 mother puts Wheezy in a yard sale, but Woody rescues him, only to be
	 stolen by a greedy toy collector, who takes him to his apartment.
	 Buzz Lightyear and the rest of Andy's toys identify the thief from a
	 commercial to be Al McWhiggin, the owner of Al's Toy Barn. Buzz, Hamm,
	 Mr. Potato Head, Slinky Dog, and Rex set out to rescue Woody.""",
	"https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg",
	"https://www.youtube.com/watch?v=h1ZMmk_yCno")

monsters_inc = media.Movie(	"Monsters, Inc.",
	"""The city of Monstropolis in the monster world is powered by energy
	 from the screams of human children. At the Monsters, Inc. factory,
	 skilled monsters employed as 'scarers' venture into the human world
	 to scare children and harvest their screams, through doors that
	 activate portals to the children's bedroom closets. It is considered
	 dangerous work, as human children are believed to be 'toxic'.
	 Energy production is falling because children are becoming less easily
	 scared, and company chairman, Henry J. Waternoose,
	 is determined to find a solution. James P. 'Sulley' Sullivan is the"
	 organization's top scarer, but his chief rival Randall Boggs is"
	 close behind.""",
	"https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
	"https://www.youtube.com/watch?v=Ue_SfrHHBAc")

finding_nemo = media.Movie(	"Finding Nemo",
	"""Two ocellaris clownfish, Marlin and Coral, admire their new home in the
	 Great Barrier Reef and their clutch of clownfish eggs when a barracuda
	 attacks, knocking Marlin unconscious. He wakes up to find that Coral
	 and all but one of the eggs have been eaten by the barracuda.
	 Marlin names this last egg Nemo, a name that Coral liked.""",
	"https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
	"https://www.youtube.com/watch?v=AXoZdTe9YFs")

the_incredibles = media.Movie( "The Incredibles",
	"""Public opinion turns against superheroes--also called 'Supers'--due to
	 collateral damage from their crime-fighting. After several lawsuits,
	 they are forced into civilian relocation programs. Fifteen years later,
	 Bob and Helen Parr, formerly known as Mr. Incredible and Elastigirl, and
	 their children Violet, Dash, and baby Jack-Jack are a suburban family.
	 Bob dislikes suburbia and his white-collar job, and with his friend
	 Lucius Best, formerly known as Frozone, occasionally relives his glory
	 days by secretly acting as vigilantes at night.""",
	"https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
	"https://www.youtube.com/watch?v=eZbzbC9285I")

cars = media.Movie(	"Cars",
	"""In a world populated by anthropomorphic vehicles, the last race of the
	 Piston Cup championship ends in a three-way tie between retiring veteran
	 Strip 'The King' Weathers, infamous runner-up Chick Hicks, and rookie
	 Lightning McQueen. The tiebreaker race is scheduled for one week later
	 at the Los Angeles International Speedway in California. McQueen is
	 desperate to win the race, since it would not only make him the first
	 rookie to win a championship, but also allow him to leave the
	 unglamorous sponsorship of Rusteze, a bumper ointment company, and
	 allow him to take The King's place as the sponsored car of the lucrative
	 Dinoco team. Eager to start practice in California as soon as possible,
	 he pushes his big rig, Mack, to travel all night long. While McQueen is
	 sleeping, Mack drifts off, and is startled by a gang of four reckless
	 street racers, causing McQueen to fall out the back of the trailer and
	 onto the road. McQueen wakes in the middle of traffic and speeds off the
	 highway to find Mack, but ends up lost in the run-down desert town of
	 Radiator Springs, while inadvertently ruining the pavement of its
	 main road.""",
	"https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
	"https://www.youtube.com/watch?v=WGByijP0Leo")

ratatouille = media.Movie(	"Ratatouille",
	"""Remy is an idealistic and ambitious young rat, gifted with highly
	 developed senses of taste and smell. Inspired by his idol, the recently
	 deceased chef Auguste Gusteau, Remy dreams of becoming a cook himself.
	 When an old French woman discovers Remy's colony in her house and
	 attempts to exterminate them, they are forced to flee, and Remy becomes
	 separated from his family in the panic. He ends up in the sewers of
	 Paris and eventually finds himself at a skylight overlooking the
	 kitchen of Gusteau's restaurant.""",
	"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=1yKqLNnxGZw")

wall_e = media.Movie(	"Wall-E",
	"""In 2805, Earth is an abandoned planet covered in trash, with its people
	 evacuated by megacorporation Buy-N-Large on giant starliners.
	 BnL has left behind WALL-E robot trash compactors to clean up; however,
	 all have since stopped functioning, except one unit who has gained
	 sentience and is able to stay active using parts from other units.
	 One day, WALL-E discovers a healthy seedling, which he returns to his
	 home. Later, an unmanned spaceship lands and deploys an EVE probe to
	 scan the planet. WALL-E is infatuated with EVE, who is initially hostile
	 but gradually befriends him. When WALL-E brings EVE to his trailer and
	 shows her the plant, however, she suddenly takes the plant and goes into
	 standby mode. WALL-E, confused, unsuccessfully tries to reactivate her.
	 The ship then returns to collect EVE, and with WALL-E clinging on,
	 returns to its mothership, the starliner Axiom.""",
	"https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
	"https://www.youtube.com/watch?v=ZisWjdjs-gM")

up = media.Movie(	"Up",
	"""In 1940, nine-year-old Carl Fredricksen idolizes famous explorer Charles
	 F. Muntz. When Muntz is accused of fabricating the skeleton of a giant
	 exotic bird he says he discovered at Paradise Falls, he vows not to
	 return until he captures one alive. One day, Carl befriends a girl named
	 Ellie, also a Muntz fan. She confides to Carl her desire to move her
	 'clubhouse'--an abandoned house in the neighborhood--to a cliff
	 overlooking Paradise Falls.""",
	"https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
	"https://www.youtube.com/watch?v=ORFWdXl_zJ4")

toy_story_3 = media.Movie(	"Toy Story 3",
	"""Seventeen-year-old Andy is about to leave for college, and his toys have
	 not been played with for years. He intends to take Woody with him,
	 and puts Buzz Lightyear, Jessie, and the other toys in a trash bag to be
	 stored in the attic. Andy's mother mistakenly takes the bag to the curb
	 for garbage pickup. The toys escape and, believing Andy intended to
	 throw them away, decide to climb into a donation box with Molly's
	 discarded toy, Barbie, bound for Sunnyside Daycare. Woody follows them,
	 but is unable to convince them of the mistake.""",
	"https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
	"https://www.youtube.com/watch?v=2BlMNH1QTeE")

cars_2 = media.Movie(	"Cars 2",
	"""Finn McMissile, a British spy, infiltrates the world's largest untapped
	 oil reserves owned by a group of lemon cars. After being discovered, he
	 flees and fakes his death. Lightning McQueen, now a four-time Piston
	 Cup champion, returns to Radiator Springs. However, Italian formula
	 race car, Francesco Bernoulli, challenges McQueen to the newly created
	 World Grand Prix, led by its creator, Sir Miles Axlerod. McQueen,
	 and his best friend Mater -- along with Luigi, Guido, Fillmore, and
	 Sarge -- depart for Tokyo for the first race of the Grand Prix.""",
	"https://upload.wikimedia.org/wikipedia/en/7/7f/Cars_2_Poster.jpg",
	"https://www.youtube.com/watch?v=oFTfAdauCOo")

brave = media.Movie(	"Brave",
	"""In Medieval Scotland, Merida, a young princess of the clan Dunbroch,
	 is given a bow and arrow by her father, King Fergus, for her birthday.
	 Her mother, Queen Elinor, disagrees with the present. While venturing
	 into the woods to fetch a stray arrow, Merida encounters a
	 will-o'-the-wisp. Soon afterward, Mor'du, a huge demon bear, attacks
	 the family. Merida flees on horseback with Elinor, while Fergus fends
	 off Mor'du, though the fight costs him one of his legs.""",
	"https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg",
	"https://www.youtube.com/watch?v=5fPmKfcaaWk")

monsters_university = media.Movie(	"Monsters University",
	"""Michael 'Mike' Wazowski, a young 7-year-old monster, aspires to become
	 a scarer (a monster who enters the human world at night to scare
	 children and harvest their screams for energy) when he grows up
	 after visiting Monsters Inc., Monstropolis' most profitable scaring
	 company, on a school field trip. Eleven years later, Mike is a
	 first-year scare major at Monsters University, where he meets fellow
	 monster, James P. 'Sulley' Sullivan. Mike studies hard, while the
	 privileged Sulley, coming from a family of talented scarers, relies
	 only on his natural ability and begins to falter. As the semester
	 progresses, Mike and Sulley attempt to join a fraternity, but only
	 Sulley is accepted into Roar Omega Roar, the strongest fraternity on
	 campus. At the semester's final exam, a fight between the two causes
	 them to accidentally break Dean Abigail Hardscrabble's cherished Scream
	 Can. Hardscrabble fails both of them immediately, stating that Sulley
	 does not study enough, and Mike is not scary enough.""",
	"https://upload.wikimedia.org/wikipedia/en/2/2a/Monsters_University_poster_3.jpg", # NOQA
	"https://www.youtube.com/watch?v=xBzPioph8CI")

inside_out = media.Movie(	"Inside Out",
	"""Riley Andersen is born in Minnesota and within her mind, five
	 personifications of her basic emotions--Joy, Sadness, Fear, Disgust,
	 and Anger--gradually come to life and influence her actions via a
	 console in her mind's Headquarters. As she grows up, her experiences
	 become memories, stored in colored orbs, which are sent into long-term
	 memory each night. Her five most important 'core memories'
	 (all of which are happy ones) are housed in a hub that each power
	 an aspect of her personality which take the form of floating islands.
	 In Headquarters, Joy acts as a de facto leader to maintain Riley's
	 cheerful childhood, but since she and the other emotions do not
	 understand Sadness' purpose, she frequently tries to keep Sadness away
	 from the console.""",
	"https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg", # NOQA
	"https://www.youtube.com/watch?v=yRUAzGQ3nSY")

the_good_dinosaur = media.Movie(	"The Good Dinosaur",
	"""In an alternate history, the asteroid that would have caused the
	 extinction of the dinosaurs 65 million years ago passes safely
	 over Earth. Sixty-five million years later, Apatosaurus farmers
	 Henry and Ida have children Libby, Buck, and the runt Arlo,
	 who has trouble adjusting to farm life. While his successful
	 siblings are allowed to 'make their mark' (a mud-print on the
	 family's corn silo), Arlo's timid nature makes tasks difficult
	 for him. Henry attempts to give Arlo a sense of purpose by putting
	 him in charge of guarding their silo, and helps him set a trap.
	 It captures a feral caveboy, but Arlo doesn't have the heart to kill
	 him, and sets him free. Disappointed, Henry takes Arlo to track the
	 caveboy, leading them into a ravine. Henry saves Arlo from a flash
	 flood before being swept away and killed.""",
	"https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg", # NOQA
	"https://www.youtube.com/watch?v=O-RgquKVTPE")

finding_dory = media.Movie(	"Finding Dory",
	"""Dory, a regal blue tang, gets separated from her parents as a child.
	 As she grows up, Dory attempts to search for them, but gradually forgets
	 them due to her short-term memory loss. In the flashback of the previous
	 film, Finding Nemo, she joins Marlin - a clownfish looking for his
	 missing son Nemo - after accidentally swimming into him.""",
	"https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
	"https://www.youtube.com/watch?v=JhvrQeY3doI")

cars_3 = media.Movie(	"Cars 3",
	"""Lightning McQueen, now a seven-time Piston Cup racing legend,
	 finds himself overshadowed by Jackson Storm, an arrogant rookie who
	 belongs to a new generation of racers that use the latest technology
	 to improve their racing performance. This causes McQueen's fellow
	 veterans to either be retired or fired by their sponsors to make way
	 for the new rookies. In the final race of the season, as he tries to
	 catch up to Storm and the other leaders, his tire blows-out and he
	 suffers a violent, nearly fatal rollover crash, leaving him badly
	 injured, while Storm becomes the new Piston Cup Champion.""",
	"https://upload.wikimedia.org/wikipedia/en/9/94/Cars_3_poster.jpg",
	"https://www.youtube.com/watch?v=2LeOH9AGJQM")

coco = media.Movie(	"Coco",
	"""The Rivera family history is told, explaining that its late matriarch
	 Imelda was the wife of a musician who left her and her child
	 to pursue a career in music. She turned to shoemaking which became
	 the family business, and began a tradition which to this day bans
	 music in the family. Her great-great-grandson, 12-year-old Miguel,
	 lives with his elderly great-grandmother Coco and the rest of her
	 descendants in the small, fictional Mexican village of Santa Cecilia.
	 He secretly dreams of becoming a musician like his idol Ernesto de la
	 Cruz, a popular singer and film star, and contemporary of Imelda.
	 When Miguel tries to enter a talent show for the Day of the Dead,
	 his grandmother Elena destroys his guitar. Miguel then discovers
	 something hidden in the photo of Mama Imelda - taken with her husband
	 and infant Coco - at the center of the family ofrenda: her husband
	 (whose face is ripped out) was holding the guitar famously used by
	 Ernesto.""",
	"https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg", # NOQA
	"https://www.youtube.com/watch?v=xlnPHQ3TLX8")

incredibles_2 = media.Movie(	"Incredibles 2",
	"""Incredibles 2 features the return of the Parrs, a family of 'Supers'
	 (humans with super abilities). This film will focus on Helen Parr,
	 also known as Elastigirl, while her husband Bob remains at home to
	 watch their children Violet, Dash, and Jack-Jack. The family
	 struggles to maintain normal lives while they remain unaware of
	 Jack-Jack's powers.""",
	"https://upload.wikimedia.org/wikipedia/en/2/27/The_Incredibles_2.jpg",
	"https://www.youtube.com/watch?v=fa6coq9JHE8")

toy_story_4 = media.Movie(	"Toy Story 4 [No Trailer Available]", 
	"""The film will focus on the romance between Woody and Bo Peep,
	 building on Bo Peep's absence from Toy Story 3,
	 with Woody and Buzz trying to find her and bring her home.""",
	"https://www.gstatic.com/tv/thumb/movieposters/12004128/p12004128_p_v8_aa.jpg", # NOQA
	#No Trailer
	"")

untitled_film = media.Movie(	"Untitled Film [No Trailer Available]",
	"TBA.",
	"https://static1.squarespace.com/static/58c6e8979f745642578bc439/t/58c6ed3b5016e1907a00aa39/1489517575818/", # NOQA
	#No Trailer
	"")

#List of all Pixar Films
##Source: https://en.wikipedia.org/wiki/List_of_Pixar_films

movies = [toy_story,
	a_bugs_life,
	toy_story_2,
	monsters_inc,
	finding_nemo,
	the_incredibles,
	cars,
	ratatouille,
	wall_e,
	up,
	toy_story_3,
	cars_2,
	brave,
	monsters_university,
	inside_out,
	the_good_dinosaur,
	finding_dory,
	cars_3,
	coco,
	incredibles_2,
	toy_story_4,
	untitled_film, # March 13, 2020
	untitled_film, # June 19, 2020
	untitled_film # June 18, 2021
]

fresh_tomatoes.open_movies_page(movies)
