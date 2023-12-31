from aiogram import types
from states.register import Medias
from aiogram.dispatcher import FSMContext
from loader import dp, bot

@dp.message_handler(commands='kidsenglish')
async def kidsenglish(message: types.Message):
    text = ("<b>Founders Language Schoolga</b> xush kelibsiz!\n\n"
            "KIDS English kurslari ning afzalliklarini sanab o'tamiz:\n\n"
            "✅ Guruhda 10 ± ta o'quvchi bo'ladi\n"
            "✅ KIDS guruhlari har bir darajada 4 oy va darslar davomiyligi 2 soatdan\n"
            "✅ Angliya metodikasi orqali ta'lim\n"
            "✅ Macmillan nashriyot kitoblari\n"
            "✅ Ota-ona nazorati uchun shaxsiy kabinet\n"
            "✅ Hero Card (ushbu Hero Card larni yig'gan holda siz <b>Founders</b> o'quv markazining qimmatbaho sov'g'alariga ega bo'lasiz)\n"
            "✅ Ikkinchi ustoz biriktriladi\n\n"
            "Ha aytgancha har oyning 2 ta yakshanba kunlari <b>jajji bolajonlarimiz</b> vaqtini behuda o'tkazmasin degan holda biz <b>bepul</b> 'event' lar o'tkazamiz\n\n"
            "😌 <b>Founders</b> da farzandigiz kelajagini birgalikda quramiz\n\n")
    
    await message.answer(text)

    text2 = ("@founders_school_uz let's grow with us!\n",
            "<b>Asosiy:</b>",
            "/start - Botni ishga tushirish",
            "/help - Shu habarni ko'rsatadi\n\n<b>Biz haqimizda:</b>",
            "/aboutus - Biz haqimizda:\n"
            "/aboutadresses - Bizning manzillar\n\n"
            "<b>Bizning kurslar:</b>\n"
            "/ieltsturbo - IELTS Turbo\n"
            "/ieltsvideo - IELTS Turbo <b>video</b>\n\n"
            "/generalenglish - General English\n"
            "/generalvideo - General English <b>video</b>\n\n"
            "/kidsenglish - KIDS English\n"
            "/kidsvideo - KIDS English <b>video</b>\n\n"
            "<b>Regestratiya:</b>\n"
            "/register - Registratsiydan o'tish\n",
            "<b>Sifat nazorati:</b>\n"
            "/suggest - Taklif va shikoyat uchun")

    await message.answer("\n".join(text2))


@dp.message_handler(commands='kidsvideo')
async def ieltsturbovideo(message: types.Message):
    video1 = 'BAACAgIAAxkBAAJEs2ScQyxu_DfCeP7lQ3uNnax3BtWEAAIZLgACW3PhSIpLKslWuHi3LwQ'

    await bot.send_video(chat_id=message.chat.id, video=video1)
