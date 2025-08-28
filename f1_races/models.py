from django.db import models

#-----------------------------------------------------------------------Tabelas Mães-------------------------------------------------------------------------------------
#Lembra de verificar quais campos podem ser ou vazios ou Blanks

class sessions(models.Model):
    year = models.IntegerField(primary_key=True)

    class Meta:
        verbose_name = 'Session'

class entrants(models.Model):
    entrantsID = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Entrant'

class continents(models.Model):
    continentsID = models.CharField(max_length=15, primary_key=True)
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Continent'

class countries(models.Model):
    countriesID = models.CharField(max_length=15, primary_key=True)
    alpha2Code = models.CharField(max_length=2)
    alpha3Code = models.CharField(max_length=3)
    iocCode = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    demonym = models.CharField(max_length=50)
    continentID = models.ForeignKey(continents, on_delete=models.CASCADE)

class circuits(models.Model):
    circuitsID = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    previousNames = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    direction = models.CharField(max_length=20)
    placeName = models.CharField(max_length=100)
    countriesID = models.ForeignKey(countries, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    length = models.FloatField()
    turns = models.IntegerField()
    totalRacesHeld = models.IntegerField()

    class Meta:
        verbose_name = 'Circuit'

class constructors(models.Model):
    constructorsID = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    countriesID = models.ForeignKey(countries, on_delete=models.CASCADE)
    bestChampionshipPosition = models.IntegerField()
    bestStartingGridPosition = models.IntegerField()
    bestRaceResult = models.IntegerField()
    totalChampionshipWins = models.IntegerField()
    totalRaceEntries = models.IntegerField()
    totalRaceStarts = models.IntegerField()
    totalRaceWins = models.IntegerField()
    total1And2Finishes = models.IntegerField()
    totalRaceLaps = models.IntegerField()
    totalPodiums = models.IntegerField()
    totalPodiumRaces = models.IntegerField()
    totalPoints = models.IntegerField()
    totalChampionshipPoints = models.IntegerField()
    totalPolePositions = models.IntegerField()
    totalFastestLaps = models.IntegerField()

    class Meta:
        verbose_name = 'Constructor'

class chassis(models.Model):
    chassisID = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Chassis'

class enginesManufacturers(models.Model):
    enginesManufacturersID = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    countriesID = models.ForeignKey(countries, on_delete=models.CASCADE)
    bestChampionshipPosition = models.IntegerField()
    bestStartingGridPosition = models.IntegerField()
    bestRaceResult = models.IntegerField()
    totalChampionshipWins = models.IntegerField()
    totalRaceEntries = models.IntegerField()
    totalRaceStarts = models.IntegerField()
    totalRaceWins = models.IntegerField()
    total1And2Finishes = models.IntegerField()
    totalRaceLaps = models.IntegerField()
    totalPodiums = models.IntegerField()
    totalPodiumRaces = models.IntegerField()
    totalPoints = models.IntegerField()
    totalChampionshipPoints = models.IntegerField()
    totalPolePositions = models.IntegerField()
    totalFastestLaps = models.IntegerField()

    class Meta:
        verbose_name = 'Engine Manufacturer'

class engines(models.Model):
    enginesID = models.CharField(max_length=15, primary_key=True)
    enginesManufacturersID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    capacity = models.IntegerField()
    configuration = models.CharField(max_length=100)
    aspiration = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Engine'

class grandPrix(models.Model):
    grandPrixID = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    shortName = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    countriesID = models.ForeignKey(countries, on_delete=models.CASCADE)
    totalRacesHeld = models.IntegerField()

    class Meta:
        verbose_name = 'Grand Prix'

class drivers(models.Model):
    driversID = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    permanentNumber = models.IntegerField()
    gender = models.CharField(max_length=10)
    dateOfBirth = models.DateField()
    dateOfDeath = models.DateField(null=True, blank=True)
    placeOfBirth = models.CharField(max_length=100)
    countryOfBirthID = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='drivers_country_of_birth')
    nationalityCountryID = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='drivers_nationality')
    secondNationalityCountryID = models.ForeignKey(countries, on_delete=models.CASCADE, related_name='drivers_second_nationality', null=True, blank=True)
    bestChampionshipPosition = models.IntegerField()
    bestStartingGridPosition = models.IntegerField()
    bestRaceResult = models.IntegerField()
    totalChampionshipWins = models.IntegerField()
    totalRaceEntries = models.IntegerField()
    totalRaceStarts = models.IntegerField()
    totalRaceWins = models.IntegerField()
    totalRaceLaps = models.IntegerField()
    totalPodiums = models.IntegerField()
    totalPoints = models.IntegerField()
    totalChampionshipPoints = models.IntegerField()
    totalPolePositions = models.IntegerField()
    totalFastestLaps = models.IntegerField()
    totalDriverOfTheDay = models.IntegerField()
    totalGrandSlams = models.IntegerField()

    class Meta:
        verbose_name = 'Driver'

class tyreManufacturers(models.Model):
    tyreManufacturersID = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    countriesID = models.ForeignKey(countries, on_delete=models.CASCADE)
    bestStartingGridPosition = models.IntegerField()
    bestRaceResult = models.IntegerField()
    totalRaceEntries = models.IntegerField()
    totalRaceStarts = models.IntegerField()
    totalRaceWins = models.IntegerField()
    totalRaceLaps = models.IntegerField()
    totalPodiums = models.IntegerField()
    totalPodiumRaces = models.IntegerField()
    totalPolePositions = models.IntegerField()
    totalFastestLaps = models.IntegerField()

    class Meta:
        verbose_name = 'Tyre Manufacturer'

class races(models.Model):
    racesID = models.CharField(max_length=15, primary_key=True)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    grandPrixID = models.ForeignKey(grandPrix, on_delete=models.CASCADE)
    officialName = models.CharField(max_length=100)
    qualifyingFormat = models.CharField(max_length=100)
    sprintQualifyingFormat = models.CharField(max_length=100)
    circuitsID = models.ForeignKey(circuits, on_delete=models.CASCADE)
    direction = models.CharField(max_length=100)
    courseLength = models.FloatField()
    turns = models.IntegerField()
    laps = models.IntegerField()
    distance = models.FloatField()
    scheduledLaps = models.IntegerField()
    scheduledDistance = models.FloatField()
    driversChampionshipDecider = models.BooleanField(default=False)
    constructorsChampionshipDecider = models.BooleanField(default=False)
    preQualifyingDate = models.DateField(null=True, blank=True)
    preQualifyingTime = models.TimeField(null=True, blank=True)
    freePractice1Date = models.DateField(null=True, blank=True)
    freePractice1Time = models.TimeField(null=True, blank=True)
    freePractice2Date = models.DateField(null=True, blank=True)
    freePractice2Time = models.TimeField(null=True, blank=True)
    freePractice3Date = models.DateField(null=True, blank=True)
    freePractice3Time = models.TimeField(null=True, blank=True)
    freePractice4Date = models.DateField(null=True, blank=True)
    freePractice4Time = models.TimeField(null=True, blank=True)
    qualifying1Date = models.DateField(null=True, blank=True)
    qualifying1Time = models.TimeField(null=True, blank=True)
    qualifying2Date = models.DateField(null=True, blank=True)
    qualifying2Time = models.TimeField(null=True, blank=True)
    qualifyingDate = models.DateField(null=True, blank=True)
    qualifyingTime = models.TimeField(null=True, blank=True)
    sprintQualifyingDate = models.DateField(null=True, blank=True)
    sprintQualifyingTime = models.TimeField(null=True, blank=True)
    sprintRaceDate = models.DateField(null=True, blank=True)
    sprintRaceTime = models.TimeField(null=True, blank=True)
    warmingUpDate = models.DateField(null=True, blank=True)
    warmingUpTime = models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Race'


#-----------------------------------------------------------------------Tabelas Filhas---------------------------------------------------------------------------------------------

class constructors_chronology(models.Model):
    parentConstructorID = models.ForeignKey(constructors,related_name= 'parentConstructorID' ,on_delete=models.CASCADE)
    positionDisplayOrder = models.IntegerField()
    constructorID = models.ForeignKey(constructors,related_name= 'constructorID' ,on_delete=models.CASCADE)
    yearFrom = models.IntegerField()
    yearTo = models.IntegerField()

    class Meta:
        verbose_name = 'Constructors Chronology'

class drivers_family_relations(models.Model):
    parentDriverID = models.ForeignKey(drivers, related_name='parentDriverID', on_delete=models.CASCADE)
    positionDisplayOrder = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='driverID', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Drivers Family Relations'

class races_constructors(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    constructorID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    points = models.IntegerField()
    positionsGained = models.IntegerField()

    class Meta:
        verbose_name = 'Races Constructors'

class races_driver_of_the_day_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    constructorID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    points = models.IntegerField()
    positionsGained = models.IntegerField()

    class Meta:
        verbose_name = 'Races Driver of the Day Results'

class races_driver_standings(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    points = models.IntegerField()
    positionsGained = models.IntegerField()

    class Meta:
        verbose_name = 'Races Driver Standings'

class races_fastest_laps(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    lap = models.IntegerField()
    time = models.DurationField()
    timeMillis = models.IntegerField()
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Races Fastest Laps'

class races_free_pratice1_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Free Practice 1 Results'

class races_free_pratice2_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Free Practice 2 Results'

class races_free_pratice3_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Free Practice 3 Results'

class races_free_pratice4_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Free Practice 4 Results'

class races_pit_stops(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    stop = models.IntegerField()
    lap = models.IntegerField()
    time = models.DurationField()
    timeMillis = models.IntegerField()

    class Meta:
        verbose_name = 'Races Pit Stops'

class races_pre_qualifying_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    q1 = models.DurationField(null=True, blank=True)
    q1Millis = models.IntegerField(null=True, blank=True)
    q2 = models.DurationField(null=True, blank=True)
    q2Millis = models.IntegerField(null=True, blank=True)
    q3 = models.DurationField(null=True, blank=True)
    q3Millis = models.IntegerField(null=True, blank=True)
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Pre Qualifying Results'

class races_qualifying1_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    q1 = models.DurationField(null=True, blank=True)
    q1Millis = models.IntegerField(null=True, blank=True)
    q2 = models.DurationField(null=True, blank=True)
    q2Millis = models.IntegerField(null=True, blank=True)
    q3 = models.DurationField(null=True, blank=True)
    q3Millis = models.IntegerField(null=True, blank=True)
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Qualifying 1 Results'

class races_qualifying2_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    q1 = models.DurationField(null=True, blank=True)
    q1Millis = models.IntegerField(null=True, blank=True)
    q2 = models.DurationField(null=True, blank=True)
    q2Millis = models.IntegerField(null=True, blank=True)
    q3 = models.DurationField(null=True, blank=True)
    q3Millis = models.IntegerField(null=True, blank=True)
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Qualifying 2 Results'

class races_qualifying_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    q1 = models.DurationField(null=True, blank=True)
    q1Millis = models.IntegerField(null=True, blank=True)
    q2 = models.DurationField(null=True, blank=True)
    q2Millis = models.IntegerField(null=True, blank=True)
    q3 = models.DurationField(null=True, blank=True)
    q3Millis = models.IntegerField(null=True, blank=True)
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Qualifying Results'

class races_race_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    sharedCar = models.BooleanField(default=False)
    laps = models.IntegerField()
    time = models.DurationField()
    timeMillis = models.IntegerField()
    timePenalty = models.DurationField(null=True, blank=True)
    timePenaltyMillis = models.IntegerField(null=True, blank=True)
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    gapLaps = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    reasonRetired = models.CharField(max_length=100, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    polePosition = models.BooleanField(default=False)
    qualificationPositionNumber = models.IntegerField(null=True, blank=True)
    qualificationPositionText = models.CharField(max_length=100, null=True, blank=True)
    gridPositionNumber = models.IntegerField(null=True, blank=True)
    gridPositionText = models.CharField(max_length=100, null=True, blank=True)
    positionGained = models.IntegerField(null=True, blank=True)
    pitStops = models.IntegerField(null=True, blank=True)
    fastestLap = models.BooleanField(default=False)
    driverOfTheDay = models.BooleanField(default=False)
    grandSlam = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Races Race Results'

class races_sprint_qualifying(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    q1 = models.DurationField(null=True, blank=True)
    q1Millis = models.IntegerField(null=True, blank=True)
    q2 = models.DurationField(null=True, blank=True)
    q2Millis = models.IntegerField(null=True, blank=True)
    q3 = models.DurationField(null=True, blank=True)
    q3Millis = models.IntegerField(null=True, blank=True)
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Sprint Qualifying'

class races_sprint_starting_grid_positions(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    qualificationPositionNumber = models.IntegerField(null=True, blank=True)
    qualificationPositionText = models.CharField(max_length=100, null=True, blank=True)
    gridPenalty = models.IntegerField()
    gridPenaltyPositions = models.IntegerField()
    time = models.DurationField()
    timeMillis = models.IntegerField()

    class Meta:
        verbose_name = 'Races Sprint Starting Grid Positions'

class races_sprint_race_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    sharedCar = models.BooleanField(default=False)
    laps = models.IntegerField()
    time = models.DurationField()
    timeMillis = models.IntegerField()
    timePenalty = models.DurationField(null=True, blank=True)
    timePenaltyMillis = models.IntegerField(null=True, blank=True)
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    gapLaps = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    reasonRetired = models.CharField(max_length=100, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    polePosition = models.BooleanField(default=False)
    qualificationPositionNumber = models.IntegerField(null=True, blank=True)
    qualificationPositionText = models.CharField(max_length=100, null=True, blank=True)
    gridPositionNumber = models.IntegerField(null=True, blank=True)
    gridPositionText = models.CharField(max_length=100, null=True, blank=True)
    positionGained = models.IntegerField(null=True, blank=True)
    pitStops = models.IntegerField(null=True, blank=True)
    fastestLap = models.BooleanField(default=False)
    driverOfTheDay = models.BooleanField(default=False)
    grandSlam = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Races Sprint Race Results'
        
class races_starting_grid_positions(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    qualificationPositionNumber = models.IntegerField(null=True, blank=True)
    qualificationPositionText = models.CharField(max_length=100, null=True, blank=True)
    gridPenalty = models.IntegerField()
    gridPenaltyPositions = models.IntegerField()
    time = models.DurationField()
    timeMillis = models.IntegerField()

    class Meta:
        verbose_name = 'Races Starting Grid Positions'

class races_warming_up_results(models.Model):
    raceID = models.ForeignKey(races, on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    timePenalty = models.DurationField(null=True, blank=True)
    timePenaltyMillis = models.IntegerField(null=True, blank=True)
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    gapLaps = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Warming Up Results'


class sessions_entrants_chassis(models.Model):
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    entrantID = models.ForeignKey(entrants, on_delete=models.CASCADE)
    constructorID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    chassisID = models.ForeignKey(chassis, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sessions Entrants Chassis'

class sessions_entrants_constructors(models.Model):
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    entrantID = models.ForeignKey(entrants, on_delete=models.CASCADE)
    constructorID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sessions Entrants Constructors'

class sessions_entrants_drivers(models.Model):
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    entrantID = models.ForeignKey(entrants, on_delete=models.CASCADE)
    driverID = models.ForeignKey(drivers, on_delete=models.CASCADE)
    constructorID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    rounds = models.IntegerField()
    roundsText = models.CharField(max_length=100)
    testDriver = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Sessions Entrants Drivers'

class sessions_entrants_engines(models.Model):
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    entrantID = models.ForeignKey(entrants, on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    engineID = models.ForeignKey(engines, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sessions Entrants Engines'

class sessions_entrants_tyres_manufacuturers(models.Model):
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    entrantID = models.ForeignKey(entrants, on_delete=models.CASCADE)
    constructorID = models.ForeignKey(constructors, on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, on_delete=models.CASCADE)
    tyreManufacturerID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sessions Entrants Tyres Manufacturers'

class sessions_tyre_manufacturers(models.Model):
    year = models.ForeignKey(sessions, on_delete=models.CASCADE)
    tyreManufacturerID = models.ForeignKey(tyreManufacturers, on_delete=models.CASCADE)
    bestStartingGridPosition = models.IntegerField()
    bestRaceResult = models.IntegerField()
    totalRaceEntries = models.IntegerField()
    totalRaceWins = models.IntegerField()
    totalRacesStarts = models.IntegerField()
    totalRaceLaps = models.IntegerField()
    totalPodiums = models.IntegerField()
    totalPodiumRaces = models.IntegerField()
    totalPolePositions = models.IntegerField()
    totalFastestLaps = models.IntegerField()

    class Meta:
        verbose_name = 'Sessions Tyre Manufacturers'
