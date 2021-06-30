"""informacje dla programu dotyczące systemu kodowania"""
#!/usr/bin/cnv python
# -*- coding: utf-8 -*-

"""importowanie kluczowych funkcji"""
from psychopy import visual, core, event
from psychopy.visual.rect import Rect
import random
import csv

"""określenie ilości wyświetlanych cyfr na każdym etapie zadania"""
N_TRIALS_TRAIN = 1
N_TRAILS_EXP1 = 2
N_TRAILS_EXP2 = 4
N_TRAILS_EXP3 = 6
acc = False
lives = 0

"""określenie przycisków reakcyjnych"""
REACTION_KEYS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

"""określenie, co ma zawierać zestaw zmiennych zapisywanych do pliku po zakończeniu badania"""
RESULTS = [["NR", "EXPERIMENT", "RT", "TRIAL_TYPE", "REACTION"]]

"""definiowanie funkcji odpowiedzialnej za rejestrowanie klawiszy"""
def reactions(keys):
    event.clearEvents()
    key = event.waitKeys(keyList=keys)
    return key[0]

"""definiowanie funkcji odpowiedzialnej za zmianę planszy tekstowej (np.: instrukcji) na następną"""
def show_text(win, info, wait_key=["space"]):
    info.draw()
    win.flip()
    reactions(wait_key)

"""definiowanie funkcji odpowiedzialnej za wyświetlanie cyfr (i informacji o tym, żeby podać cyfry, żeby nie definiować nowej funkcji do tego)"""
def show_digit(win, info):
    info.draw()
    win.flip()

"""definiowanie funkcji odpowiedzialnej za część eksperymentalną"""
def part_of_experiment(n_trials, exp, fix):
    global acc
    global lives
    global task
    task = []
    for i in range(n_trials):
        stim_type = random.choice(list(stim.keys()))
        task.append(stim_type)
        digit = visual.TextStim(win=window, text=stim_type)
        show_digit(win=window, info=digit)
        window.callOnFlip(clock.reset)
        core.wait(1)
        window.flip()
    RESULTS.append([n_trials, exp, "Task", task, "Task"])

"""definiowanie funkcji odpowiedzialnej za zebranie reakcji od badanego"""
def answer(n_trials, exp, fix):
    global ans
    global acc
    ans = []
    for j in range(n_trials):
        key = reactions(REACTION_KEYS)
        ans.append(key)
        rt = clock.getTime()
    RESULTS.append([n_trials, exp, rt, task, ans])
    if (ans == task):
        acc = True

"""ustalenie koloru i rozmiaru okna"""
window = visual.Window(units="pix", color="black", fullscr=False)

"""ustalenie widoczności kursora"""
window.setMouseVisible(False)

"""zdefiniowanie zegara"""
clock = core.Clock()

"""określenie puli wyświetlanych bodźców (cyfr do zapamiętania)"""
stim = {"0": visual.TextStim(win=window, text="0", height=24, color="white", font="Arial", bold=True),
        "1": visual.TextStim(win=window, text="1", height=24, color="white", font="Arial", bold=True),
        "2": visual.TextStim(win=window, text="2", height=24, color="white", font="Arial", bold=True),
        "3": visual.TextStim(win=window, text="3", height=24, color="white", font="Arial", bold=True),
        "4": visual.TextStim(win=window, text="4", height=24, color="white", font="Arial", bold=True),
        "5": visual.TextStim(win=window, text="5", height=24, color="white", font="Arial", bold=True),
        "6": visual.TextStim(win=window, text="6", height=24, color="white", font="Arial", bold=True),
        "7": visual.TextStim(win=window, text="7", height=24, color="white", font="Arial", bold=True),
        "8": visual.TextStim(win=window, text="8", height=24, color="white", font="Arial", bold=True),
        "9": visual.TextStim(win=window, text="9", height=24, color="white", font="Arial", bold=True)}

"""określenie punktu fiksacji"""
fix = visual.TextStim(win=window, text="+", height=40)

"""określenie parametrów wyświetlanych komunikatów"""
inst_task = visual.TextStim(win=window, text="Wprowadź ciąg cyfr", color="white", font="Arial", height=24, bold=False)
inst1 = visual.TextStim(win=window, text="Instrukcja \n\n Na ekranie będą pojawiać się kolejne cyfry, Pani/Pana zadaniem jest je zapamiętać oraz odtworzyć ich kolejność po zakończeniu każdego etapu. \n\n Aby przejść dalej, wciśnij spację.", color="white", font="Arial", height=24, bold=False)
inst2 = visual.TextStim(win=window, text="Część treningowa", color="white", font="Arial", height=24, bold=False)
inst3 = visual.TextStim(win=window, text="Eksperyment - Poziom 1", color="white", font="Arial", height=24, bold=False)
inst4 = visual.TextStim(win=window, text="Eksperyment - Poziom 2", color="white", font="Arial", height=24, bold=False)
inst5 = visual.TextStim(win=window, text="Eksperyment - Poziom 3", color="white", font="Arial", height=24, bold=False)
inst_end = visual.TextStim(win=window, text="Dziękujemy za udział w badaniu", color="white", font="Arial", height=24, bold=False)

"""uruchamia poszczególne elementy eksperymentu"""
show_text(win=window, info=inst1) #informacja z instrukcją
while (acc == False): #warunek, po niespełnieniu którego pętla się nie wykona
    # TRAINING
    show_text(win=window, info=inst2) #informacja dotycząca poziomu
    part_of_experiment(N_TRIALS_TRAIN, exp=False, fix=fix) #wywołanie etapu ukazującego dany ciąg
    show_digit(win=window, info=inst_task) #informacja dotycząca zadania
    answer(N_TRIALS_TRAIN, exp=False, fix=fix) #wywołanie etapu zbierającego dane od badanego
acc = False #ustawia wartość acc na False, aby uruchomiła się następna pętla
while (acc == False):
    # EXPERIMENT_LV1
    if (lives > 2): #zatrzymuje pętlę po osiągnięciu odpowiedniej liczby prób
        break
    lives += 1
    show_text(win=window, info=inst3)
    part_of_experiment(N_TRAILS_EXP1, exp=True, fix=fix)
    show_digit(win=window, info=inst_task)
    answer(N_TRAILS_EXP1, exp=True, fix=fix)
acc = False
while (acc == False):
    # EXPERIMENT_LV2
    if (lives > 2):
        break
    lives += 1
    show_text(win=window, info=inst4)
    part_of_experiment(N_TRAILS_EXP2, exp=True, fix=fix)
    show_digit(win=window, info=inst_task)
    answer(N_TRAILS_EXP2, exp=True, fix=fix)
acc = False
while (acc == False):
    # EXPERIMENT_LV3
    if (lives > 2):
        break
    lives += 1
    show_text(win=window, info=inst5)
    part_of_experiment(N_TRAILS_EXP3, exp=True, fix=fix)
    show_digit(win=window, info=inst_task)
    answer(N_TRAILS_EXP3, exp=True, fix=fix)

# THE END
show_text(win=window, info=inst_end)

"""zapis wyników do pliku"""
with open("result.csv", "w", newline='') as f:
    write = csv.writer(f)
    write.writerows(RESULTS)
    