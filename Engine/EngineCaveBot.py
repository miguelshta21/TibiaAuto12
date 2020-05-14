import json
import time

from Conf.Hotkeys import Hotkey
from Engine.HookWindow import IsFocused

from Engine.CheckWaypoint import *
from Engine.SetFollow import SetFollow
from Engine.NumberOfTargets import NumberOfTargets
from Engine.AttackTarget import AttackTarget
from Engine.CheckWaypoint import CheckWaypoint
from Engine.TakeLoot import GetLoot

TargetNumber = 0


def EngineCaveBot(data, i, MapPosition, BattlePosition, monster, SQMs, MOUSE_OPTION, HOOK_OPTION, ScriptName):
    SendToClient = Hotkey(MOUSE_OPTION)

    MarkLocation = [0, 0]
    global TargetNumber
    if HOOK_OPTION == 0:
        import pyautogui

        MarkLocation = pyautogui.locateCenterOnScreen('images/MapSettings/' + data[i]["mark"] + '.png',
                                                      region=(
                                                      MapPosition[0], MapPosition[1], MapPosition[2], MapPosition[3]),
                                                      confidence=0.8)
        if data[i]['status'] is True and MarkLocation is not None:

            if MOUSE_OPTION == 1:
                mp = SendToClient.Position()
            else:
                mp = [0, 0]
            SendToClient.LeftClick(MarkLocation[0], MarkLocation[1])
            if MOUSE_OPTION == 1:
                SendToClient.MoveTo(mp[0], mp[1])

            number = NumberOfTargets(BattlePosition, monster, HOOK_OPTION)
            time.sleep(2.5)
            while number > 0:
                TargetNumber = AttackTarget(monster, BattlePosition, SQMs, TargetNumber, MOUSE_OPTION, HOOK_OPTION)

                follow_x_pos, follow_y_pos = SetFollow(HOOK_OPTION)

                if follow_x_pos != 0 and follow_y_pos != 0:

                    if MOUSE_OPTION == 1:
                        mp = SendToClient.Position()
                    else:
                        mp = [0, 0]
                    SendToClient.LeftClick(follow_x_pos[0], follow_y_pos[1])
                    if MOUSE_OPTION == 1:
                        SendToClient.MoveTo(mp[0], mp[1])

                time.sleep(.3)

                TargetNumber2 = AttackTarget(monster, BattlePosition, SQMs, TargetNumber, MOUSE_OPTION, HOOK_OPTION)

                if TargetNumber2 < TargetNumber:
                    GetLoot('right', MOUSE_OPTION).TakeLoot(SQMs)

                time.sleep(0.3)

                number = NumberOfTargets(BattlePosition, monster, HOOK_OPTION)
                if number == 0:
                    break

            if CheckWaypoint(data[i]["mark"], MapPosition, HOOK_OPTION):
                data[i]['status'] = False
                if i+1 == len(data):
                    data[i-i]['status'] = True
                else:
                    data[i+1]['status'] = True
                with open('Scripts/ratThais.json', 'w') as wJson:
                    json.dump(data, wJson, indent=4)
            else:
                EngineCaveBot(data, i, MapPosition, BattlePosition, monster, SQMs, MOUSE_OPTION, HOOK_OPTION, ScriptName)
        else:
            print("Error to locate: " + data[i]["mark"])

    elif HOOK_OPTION == 1:
        from Engine.HookWindow import LocateCenterImage

        while not IsFocused():
            print("The Tibia's Window Is Not Focused !!")
            time.sleep(.3)

        while MarkLocation[0] == 0 and MarkLocation[1] == 0:
            try:
                MarkLocation[0], MarkLocation[1] = LocateCenterImage('images/MapSettings/' + data[i]["mark"] + '.png',
                                                                     Region=(
                                                                         MapPosition[0], MapPosition[1], MapPosition[2],
                                                                         MapPosition[3]),
                                                                     Precision=0.8)
            except Exception:
                MarkLocation[0] = 0
                MarkLocation[1] = 0
                print("Try Find a Mark ", data[i]["mark"])
                pass

        MarkLocation[0] = MapPosition[0] + MarkLocation[0]
        MarkLocation[1] = MapPosition[1] + MarkLocation[1]
        if data[i]['status'] is True and MarkLocation[0] != 0 and MarkLocation[1] != 0:

            if MOUSE_OPTION == 1:
                mp = SendToClient.Position()
            else:
                mp = [0, 0]
            SendToClient.LeftClick(MarkLocation[0], MarkLocation[1])
            if MOUSE_OPTION == 1:
                SendToClient.MoveTo(mp[0], mp[1])

            number = Numbers(BattlePosition, monster, HOOK_OPTION)

            time.sleep(2.5)
            while number > 0:
                try:
                    TargetNumber = NumbersOfTarget(monster, BattlePosition, SQMs, TargetNumber, MOUSE_OPTION, HOOK_OPTION)
                except Exception:
                    TargetNumber = 0
                    pass

                try:
                    follow_x_pos, follow_y_pos = SetFollow(HOOK_OPTION)
                except Exception:
                    follow_x_pos = 0
                    follow_y_pos = 0
                    pass

                if follow_x_pos != 0 and follow_y_pos != 0:

                    if MOUSE_OPTION == 1:
                        mp = SendToClient.Position()
                    else:
                        mp = [0, 0]
                    SendToClient.LeftClick(follow_x_pos, follow_y_pos)
                    if MOUSE_OPTION == 1:
                        SendToClient.MoveTo(mp[0], mp[1])

                time.sleep(.3)

                try:
                    TargetNumber2 = NumbersOfTarget(monster, BattlePosition, SQMs, TargetNumber, MOUSE_OPTION, HOOK_OPTION)
                except Exception:
                    TargetNumber2 = 0
                    pass

                if TargetNumber2 < TargetNumber:
                    GetLoot('right', MOUSE_OPTION).TakeLoot(SQMs)

                time.sleep(0.3)

                number = Numbers(BattlePosition, monster, HOOK_OPTION)

                if number == 0:
                    break

            if CheckWaypoint(data[i]["mark"], MapPosition, HOOK_OPTION):
                data[i]['status'] = False
                if i + 1 == len(data):
                    data[i - i]['status'] = True
                    with open('Scripts/' + ScriptName + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
                else:
                    data[i + 1]['status'] = True
                    with open('Scripts/' + ScriptName + '.json', 'w') as wJson:
                        json.dump(data, wJson, indent=4)
            else:
                EngineCaveBot(data, i, MapPosition, BattlePosition, monster, SQMs, MOUSE_OPTION, HOOK_OPTION, ScriptName)
        else:
            print("Error to locate: " + data[i]["mark"])


def Numbers(BattlePosition, monster, HOOK_OPTION):
    Except = True
    while Except:
        try:
            number = NumberOfTargets(BattlePosition, monster, HOOK_OPTION)
            Except = False
            return number
        except Exception:
            Except = True
            pass


def NumbersOfTarget(monster, BattlePosition, SQMs, TargetNumber, MOUSE_OPTION, HOOK_OPTION):
    Except = True
    while Except:
        try:
            ReturnedNumber = AttackTarget(monster, BattlePosition, SQMs, TargetNumber, MOUSE_OPTION, HOOK_OPTION)
            Except = False
            return ReturnedNumber
        except Exception:
            Except = True
            pass
