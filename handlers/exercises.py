from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.handler import Order, get_exercise
from model.Model import InputModel, TestModel

router = Router()




@router.message(Command("grammar"))
async def grammar(message: Message, state: FSMContext):

    data = {
        "The freezing rain was chilly and unpleasant, but then, what could you expect in the middle of December? It was after she had run 17 km that she ______________.(FALL)": "FELL",
        "The island has an area of 49 square kilometres, the biggest part of which _ by a glacier.(COVER)": "ISCOVER",
        "However, there are still about 200 impressive buildings and structures, ______________ palaces, plazas, houses, temples and even an observatory for studying the sun and stars.(INCLUDE)": "INCLUDING",
        "He came home and told his mother that he,_______the best plant. (GROW)": "WOULDGROW",
        "She helped __ plant the seed. Every day he watered it but nothing grew.(HE)": "HIM",
        "The emperor said, «Lying is the __ thing in the world. I gave you all spoilt seeds. Nothing grows from spoilt seeds.» (BAD)": "WORST",
        "He ran the ________ advertisement for the beverage on May 29 of the same year in the Atlanta Journal.(ONE)": "FIRST",
        "That's how the world famous drink ______.(INVENT)": "WASINVENTED",
        "He was the__________prominent doctor to make a strong link between the use of antiseptics and improving survival rates of wounded people. (ONE)": "FIRST",
        "His work was taken up by others, such as Joseph Lister, who _____ a pioneer of antiseptic surgery.(BECOME)": "BECAME",


    }

    await set_model(message, state, InputModel(data))


@router.message(Command("word_formation"))
async def vocabulary(message: Message, state: FSMContext):
    data = {
        "The rodeo is a really exciting event. It is a thrilling _____ between cowboys from all over the country.(COMPETE)": "COMPETITION",
        "It has a long tradition and even today there are rodeo schools which keep it alive and ______.(PROFESSION)": "PROFESSIONAL",
        "The rodeo is a spectacular sight. If a ___ has a place in the first row of the arena, he or she may even be sprinkled with sand by the passing horses.(VISIT)": "VISITOR",
        "The ______ usually starts with an opening ceremony by horsemen dressed in bright colours and carrying flags.(PERFORM)": "PERFORMANCE",
        "The city enjoys an oceanic climate, which is _____ to the climate in most of Europe.(COMPARE)": "COMPARABLE",
        "Nothing can _________ you about Auckland, which is why it is a popular destination for numerous immigrants to New Zealand.(APPOINT)": "DISAPPOINT",
        "Surprisingly enough, old factories and plants have become __ to French tourism. In France, every year, no fewer than 1400 companies, heritage museums or industrial sites draw 20 million visitors.(IMPORTANCE)": "IMPORTANT",
        "It is __ the giants of the food and agricultural industry together with the traditional crafts that have the most appeal.(GENERAL)": "GENERALLY",

    }

    await set_model(message, state, InputModel(data))


@router.message(Command("vocabulary"))
async def vocabulary(message: Message, state: FSMContext):

    data = {
        "Cedric __ knowing Tabitha with no sign of embarrassment or reluctance.": (1, ["Agreed", "Admitted", "Accepted", "Adopted"]),
        "My job was a good one and I hated to give it __ unceremoniously, but Kevin was pushing hard.": (2, ["On", "In", "Up", "To"]),
        "It would definitely __ you feel as an honored guest.": (3, ["Hold", "Take", "Keep", "Make"]),
        "The décor was resolutely Western, its furnishings assembled to ___ the effect.": (2, ["Bring", "Fulfill", "Create", "Do"]),
        "__, he asked after a while if he could order for her.": (3, ["Otherwise", "However", "Although", "Therefore"]),
        "Max White tapped on Paul's office door at 15.00. He walked in without  __ for a response.": (3, ["Requiring", "Demanding", "Expecting", "Waiting"]),
        "She was __ the guests greet each other and share the news. Vicky thought of her sister-in-law Kathleen, not present tonight.": (2, ["Looking", "Staring", "Watching", "Gazing"]),
        "She __ to do it before the war and she was doing it now, when the war was over.": (0, ["Used", "Kept", "Held", "Took"]),
        "But how did she __ to get all of those cups?": (0, ["Manage", "Achieve", "Complete", "Succeed"]),
        "The colours of its stone walls can take your breath __.": (3, ["Off", "Apart", "In", "Away"]),
        "The widest spot of the canyon is 29 kilometers __!": (0, ["Across", "Over", "Opposite", "Cross"]),
        "It felt cold ______the touch.": (1, ["For", "To", "On", "From"]),
        "At least, Tanon presumed it was precious, but now he had a decision to __.": (1, ["Do", "Make", "Have", "Get"])


    }

    await set_model(message, state, TestModel(data))






async def set_model(message: Message, state: FSMContext, model):
    await state.update_data(MyModel=model)
    await state.set_state(Order.get_exercise)
    await get_exercise(message, state)
