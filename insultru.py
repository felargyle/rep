

from .. import loader

import logging
import random


logger = logging.getLogger(__name__)


def register(cb):
    cb(InsultMod())


class InsultMod(loader.Module):
    """Shouts at people"""
    def __init__(self):
        self.name = _("Insulter")

    async def insultcmd(self, message):
        """Use when angry"""
        # TODO localisation?
        adjectives_start = ["вонючий", "жирный", "чертов", "говняный", "тупой", "блядский", "омежный", "мелкий"
                           "блядский", "жидоебский", "многопиздный", "пиздецкий", "пиздоебищный", "шароебищийся", "хуйовый", "уебищенский", "уебский", 
                          "распиздяйский" ]
        adjectives_mid = ["маленький", "выебистый", "тупой", "аутсайдер", "козлоебский", "ебаный", "пиздабольский"]
        nouns = ["далбаеб", "свинья", "педофил", "омеган", "нижний", "мудак", "жополиз", "куколд",
                 "ХУЙ", "хуеголовый", "флейтист", "идиот", "пидарас", "лузер", "хуесос", "додик", "козлоебище",
                "еблан", "гомик", "пидр", "пидар", "очкошник", "аутист", "даун", "сука", "гандон", "дерьмохеропиздократ"]
        starts = ["Ты", "Отъебись", "Когда ты сдохнешь,", "Слушай ты,", 
                  "Что с тобой не так", "Съеби", "Пососи", "Поешь говна", "Папей говна", "", ]
        ends = ["!!!!", "!", "", ")))", ")", "=)"] 
        start = random.choice(starts)
        adjective_start = random.choice(adjectives_start)
        adjective_mid = random.choice(adjectives_mid)
        noun = random.choice(nouns)
        end = random.choice(ends)
        insult = start + " " + adjective_start + " " + adjective_mid + (" " if adjective_mid else "") + noun + noun + end
        logger.debug(insult)
        await message.edit(insult)
