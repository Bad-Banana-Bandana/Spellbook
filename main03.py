import Spellbook03


def main():
    Spellbook03.IntEx()
    nameList, strList, dexList, conList,intList, wisList, chaList, levelList, skAcroList, skAnHnList, skArcaList, skAthlList, skDeceList, skHistList, skInsiList, skIntiList, skInveList, skMediList, skNatuList, skPercList, skPerfList, skPersList, skReliList, skSloHList, skSteaList, skSurvList, stStrList, stDexList, stConList, stIntList, stWisList, stChaList, characterCount, tableContents = Spellbook03.ReadProfiles()
    profileChoice = Spellbook03.PickProfile(nameList, characterCount)
    if profileChoice == 0:
        charInfo = Spellbook03.CreateProfile()
        Spellbook03.DisplayCreateProfile(charInfo)
        counter = Spellbook03.AskEditProfile()
        while counter != 0:
            charInfo = Spellbook03.EditProfile(counter, charInfo)
            Spellbook03.DisplayCreateProfile(charInfo)
            counter = Spellbook03.AskEditProfile()
            Spellbook03.SaveClose(charInfo)

    else:
        #Go to B
        pass

main()
