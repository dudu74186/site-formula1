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
    continentID = models.ForeignKey(continents, related_name='countries_continentID', on_delete=models.CASCADE)

class circuits(models.Model):
    circuitsID = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    previousNames = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    direction = models.CharField(max_length=20)
    placeName = models.CharField(max_length=100)
    countriesID = models.ForeignKey(countries, related_name='circuits_countriesID', on_delete=models.CASCADE)
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
    countriesID = models.ForeignKey(countries, related_name='constructors_countriesID', on_delete=models.CASCADE)
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
    constructorsID = models.ForeignKey(constructors, related_name='chassis_constructorsID', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Chassis'

class enginesManufacturers(models.Model):
    enginesManufacturersID = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    countriesID = models.ForeignKey(countries, related_name='engines_manufacturers_countriesID', on_delete=models.CASCADE)
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
    enginesManufacturersID = models.ForeignKey(enginesManufacturers, related_name='engines_enginesManufacturersID', on_delete=models.CASCADE)
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
    countriesID = models.ForeignKey(countries, related_name='grand_prix_countriesID', on_delete=models.CASCADE)
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
    countriesID = models.ForeignKey(countries, related_name='tyre_manufacturers_countriesID', on_delete=models.CASCADE)
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
    year = models.ForeignKey(sessions,related_name='races_year', on_delete=models.CASCADE)
    round = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    grandPrixID = models.ForeignKey(grandPrix, related_name='races_grandPrixID', on_delete=models.CASCADE)
    officialName = models.CharField(max_length=100)
    qualifyingFormat = models.CharField(max_length=100)
    sprintQualifyingFormat = models.CharField(max_length=100)
    circuitsID = models.ForeignKey(circuits, related_name='races_circuitsID', on_delete=models.CASCADE)
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
    raceID = models.ForeignKey(races, related_name='races_constructors', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_constructors', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    constructorID = models.ForeignKey(constructors, related_name='races_constructors_constructorID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_constructors_engineManufacturerID', on_delete=models.CASCADE)
    points = models.IntegerField()
    positionsGained = models.IntegerField()

    class Meta:
        verbose_name = 'Races Constructors'

class races_constructors_standings(models.Model):
    raceID = models.ForeignKey(races, related_name='races_constructors_standings', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_constructors_standings', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    constructorID = models.ForeignKey(constructors, related_name='races_constructors_standings_constructorID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_constructors_standings_engineManufacturerID', on_delete=models.CASCADE)
    points = models.IntegerField()
    positionsGained = models.IntegerField()

class races_driver_of_the_day_results(models.Model):
    raceID = models.ForeignKey(races, related_name='races_driver_of_the_day_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_driver_of_the_day_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    constructorID = models.ForeignKey(constructors, related_name='races_driver_of_the_day_results_constructorID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_driver_of_the_day_results_engineManufacturerID', on_delete=models.CASCADE)
    points = models.IntegerField()
    positionsGained = models.IntegerField()

    class Meta:
        verbose_name = 'Races Driver of the Day Results'

class races_driver_standings(models.Model):
    raceID = models.ForeignKey(races, related_name='races_driver_standings', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_driver_standings', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverID = models.ForeignKey(drivers, related_name='races_driver_standings_driverID', on_delete=models.CASCADE)
    points = models.IntegerField()
    positionsGained = models.IntegerField()

    class Meta:
        verbose_name = 'Races Driver Standings'

class races_fastest_laps(models.Model):
    raceID = models.ForeignKey(races, related_name='races_fastest_laps', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_fastest_laps', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_fastest_laps_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_fastest_laps_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_fastest_laps_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_fastest_laps_tyresManufacturerID', on_delete=models.CASCADE)
    lap = models.IntegerField()
    time = models.DurationField()
    timeMillis = models.IntegerField()
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Races Fastest Laps'

class races_free_practice1_results(models.Model):
    raceID = models.ForeignKey(races, related_name='races_free_practice1_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_free_practice1_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_free_practice1_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_free_practice1_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_free_practice1_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_free_practice1_results_tyresManufacturerID', on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Free Practice 1 Results'

class races_free_practice2_results(models.Model):
    raceID = models.ForeignKey(races, related_name='races_free_practice2_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_free_practice2_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_free_practice2_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_free_practice2_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_free_practice2_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_free_practice2_results_tyresManufacturerID', on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Free Practice 2 Results'

class races_free_practice3_results(models.Model):
    raceID = models.ForeignKey(races, related_name='races_free_practice3_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_free_practice3_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_free_practice3_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_free_practice3_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_free_practice3_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_free_practice3_results_tyresManufacturerID', on_delete=models.CASCADE)
    time = models.DurationField()
    timeMillis = models.IntegerField()
    gap = models.DurationField(null=True, blank=True)
    gapMillis = models.IntegerField(null=True, blank=True)
    interval = models.DurationField(null=True, blank=True)
    intervalMillis = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField()

    class Meta:
        verbose_name = 'Races Free Practice 3 Results'

class races_free_practice4_results(models.Model):
    raceID = models.ForeignKey(races, related_name='races_free_practice4_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_free_practice4_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_free_practice4_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_free_practice4_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_free_practice4_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_free_practice4_results_tyresManufacturerID', on_delete=models.CASCADE)
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
    raceID = models.ForeignKey(races, related_name='races_pit_stops', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_pit_stops', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_pit_stops_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_pit_stops_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_pit_stops_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_pit_stops_tyresManufacturerID', on_delete=models.CASCADE)
    stop = models.IntegerField()
    lap = models.IntegerField()
    time = models.DurationField()
    timeMillis = models.IntegerField()

    class Meta:
        verbose_name = 'Races Pit Stops'

class races_pre_qualifying_results(models.Model):
    raceID = models.ForeignKey(races, related_name='races_pre_qualifying_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_pre_qualifying_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_pre_qualifying_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_pre_qualifying_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_pre_qualifying_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_pre_qualifying_results_tyresManufacturerID', on_delete=models.CASCADE)
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
    raceID = models.ForeignKey(races, related_name='races_qualifying1_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_qualifying1_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_qualifying1_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_qualifying1_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_qualifying1_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_qualifying1_results_tyresManufacturerID', on_delete=models.CASCADE)
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
    raceID = models.ForeignKey(races, related_name='races_qualifying2_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_qualifying2_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_qualifying2_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_qualifying2_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_qualifying2_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_qualifying2_results_tyresManufacturerID', on_delete=models.CASCADE)
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
    raceID = models.ForeignKey(races, related_name='races_qualifying_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_qualifying_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_qualifying_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_qualifying_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_qualifying_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_qualifying_results_tyresManufacturerID', on_delete=models.CASCADE)
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
    raceID = models.ForeignKey(races, related_name='races_race_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_race_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_race_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_race_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_race_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_race_results_tyresManufacturerID', on_delete=models.CASCADE)
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
    raceID = models.ForeignKey(races, related_name='races_sprint_qualifying', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_sprint_qualifying', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_sprint_qualifying_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_sprint_qualifying_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_sprint_qualifying_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_sprint_qualifying_tyresManufacturerID', on_delete=models.CASCADE)
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
    raceID = models.ForeignKey(races, related_name='races_sprint_starting_grid_positions', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_sprint_starting_grid_positions', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_sprint_starting_grid_positions_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_sprint_starting_grid_positions_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_sprint_starting_grid_positions_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_sprint_starting_grid_positions_tyresManufacturerID', on_delete=models.CASCADE)
    qualificationPositionNumber = models.IntegerField(null=True, blank=True)
    qualificationPositionText = models.CharField(max_length=100, null=True, blank=True)
    gridPenalty = models.IntegerField()
    gridPenaltyPositions = models.IntegerField()
    time = models.DurationField()
    timeMillis = models.IntegerField()

    class Meta:
        verbose_name = 'Races Sprint Starting Grid Positions'

class races_sprint_race_results(models.Model):
    raceID = models.ForeignKey(races, related_name='races_sprint_race_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_sprint_race_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_sprint_race_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_sprint_race_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_sprint_race_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_sprint_race_results_tyresManufacturerID', on_delete=models.CASCADE)
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
    raceID = models.ForeignKey(races, related_name='races_starting_grid_positions', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_starting_grid_positions', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_starting_grid_positions_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_starting_grid_positions_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_starting_grid_positions_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_starting_grid_positions_tyresManufacturerID', on_delete=models.CASCADE)
    qualificationPositionNumber = models.IntegerField(null=True, blank=True)
    qualificationPositionText = models.CharField(max_length=100, null=True, blank=True)
    gridPenalty = models.IntegerField()
    gridPenaltyPositions = models.IntegerField()
    time = models.DurationField()
    timeMillis = models.IntegerField()

    class Meta:
        verbose_name = 'Races Starting Grid Positions'

class races_warming_up_results(models.Model):
    raceID = models.ForeignKey(races, related_name='races_warming_up_results', on_delete=models.CASCADE)
    year = models.ForeignKey(sessions, related_name='year_races_warming_up_results', on_delete=models.CASCADE)
    round = models.IntegerField()
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverNumber = models.IntegerField()
    driverID = models.ForeignKey(drivers, related_name='races_warming_up_results_driverID', on_delete=models.CASCADE)
    constructorsID = models.ForeignKey(constructors, related_name='races_warming_up_results_constructorsID', on_delete=models.CASCADE)
    engineManufacturerID = models.ForeignKey(enginesManufacturers, related_name='races_warming_up_results_engineManufacturerID', on_delete=models.CASCADE)
    tyreManufacturersID = models.ForeignKey(tyreManufacturers, related_name='races_warming_up_results_tyresManufacturerID', on_delete=models.CASCADE)
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
    year = models.ForeignKey(sessions, related_name='year_sessions_entrants_chassis', on_delete=models.CASCADE)
    entrantID = models.ForeignKey(entrants, related_name='sessions_entrants_chassis_entrantID', on_delete=models.CASCADE)
    constructorID = models.ForeignKey(constructors, related_name='sessions_entrants_chassis_constructorID', on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, related_name='sessions_entrants_chassis_enginesManufacturerID', on_delete=models.CASCADE)
    chassisID = models.ForeignKey(chassis, related_name='sessions_entrants_chassis_chassisID', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sessions Entrants Chassis'

class sessions_entrants_constructors(models.Model):
    year = models.ForeignKey(sessions, related_name='year_sessions_entrants_constructors', on_delete=models.CASCADE)
    entrantID = models.ForeignKey(entrants, related_name='sessions_entrants_constructors_entrantID', on_delete=models.CASCADE)
    constructorID = models.ForeignKey(constructors, related_name='sessions_entrants_constructors_constructorID', on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, related_name='sessions_entrants_constructors_enginesManufacturerID', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sessions Entrants Constructors'

class sessions_entrants_drivers(models.Model):
    year = models.ForeignKey(sessions, related_name='year_sessions_entrants_drivers', on_delete=models.CASCADE)
    entrantID = models.ForeignKey(entrants, related_name='sessions_entrants_drivers_entrantID', on_delete=models.CASCADE)
    driverID = models.ForeignKey(drivers, related_name='sessions_entrants_drivers_driverID', on_delete=models.CASCADE)
    constructorID = models.ForeignKey(constructors, related_name='sessions_entrants_drivers_constructorID', on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, related_name='sessions_entrants_drivers_enginesManufacturerID', on_delete=models.CASCADE)
    rounds = models.IntegerField()
    roundsText = models.CharField(max_length=100)
    testDriver = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Sessions Entrants Drivers'

class sessions_entrants_engines(models.Model):
    year = models.ForeignKey(sessions, related_name='year_sessions_entrants_engines', on_delete=models.CASCADE)
    entrantID = models.ForeignKey(entrants, related_name='sessions_entrants_engines_entrantID', on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, related_name='sessions_entrants_engines_enginesManufacturerID', on_delete=models.CASCADE)
    engineID = models.ForeignKey(engines, related_name='sessions_entrants_engines_engineID', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sessions Entrants Engines'

class sessions_entrants_tyres_manufacturers(models.Model):
    year = models.ForeignKey(sessions, related_name='year_sessions_entrants_tyres_manufacturers', on_delete=models.CASCADE)
    entrantID = models.ForeignKey(entrants, related_name='sessions_entrants_tyres_manufacturers_entrantID', on_delete=models.CASCADE)
    constructorID = models.ForeignKey(constructors, related_name='sessions_entrants_tyres_manufacturers_constructorID', on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, related_name='sessions_entrants_tyres_manufacturers_enginesManufacturerID', on_delete=models.CASCADE)
    tyreManufacturerID = models.ForeignKey(tyreManufacturers, related_name='sessions_entrants_tyres_manufacturers_tyresManufacturerID', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sessions Entrants Tyres Manufacturers'

class sessions_tyre_manufacturers(models.Model):
    year = models.ForeignKey(sessions, related_name='year_sessions_tyre_manufacturers', on_delete=models.CASCADE)
    tyreManufacturerID = models.ForeignKey(tyreManufacturers, related_name='sessions_tyre_manufacturers_tyresManufacturerID', on_delete=models.CASCADE)
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

class sessions_constructors(models.Model):
    year = models.ForeignKey(sessions, related_name='year_sessions_constructors', on_delete=models.CASCADE)
    constructorID = models.ForeignKey(constructors, related_name='sessions_constructors_constructorID', on_delete=models.CASCADE)
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    bestStartingGridPosition = models.IntegerField()
    bestRaceResult = models.IntegerField()
    totalRaceEntries = models.IntegerField()
    totalRaceWins = models.IntegerField()
    total1And2Finishes = models.IntegerField()
    totalRacesLaps = models.IntegerField()
    totalPodiums = models.IntegerField()
    totalPodiumRaces = models.IntegerField()
    totalPoints = models.IntegerField()
    totalPolePositions = models.IntegerField()
    totalFastestLaps = models.IntegerField()

    class Meta:
        verbose_name = 'Sessions Constructors'

class sessions_constructors_standings(models.Model):
    year = models.ForeignKey(sessions, related_name='year_sessions_constructors_standings', on_delete=models.CASCADE)
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    constructorID = models.ForeignKey(constructors, related_name='sessions_constructors_standings_constructorID', on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, related_name='sessions_constructors_standings_enginesManufacturerID', on_delete=models.CASCADE)
    points = models.IntegerField()

    class Meta:
        verbose_name = 'Sessions Constructors Standings'

class sessions_drivers(models.Model):
    year = models.ForeignKey(sessions, related_name='year_sessions_drivers', on_delete=models.CASCADE)
    driverID = models.ForeignKey(drivers, related_name='sessions_drivers_driverID', on_delete=models.CASCADE)
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    bestStartingGridPosition = models.IntegerField()
    bestRaceResult = models.IntegerField()
    totalRaceEntries = models.IntegerField()
    totalRaceStarts = models.IntegerField()
    totalRaceWins = models.IntegerField()
    totalRaceLaps = models.IntegerField()
    totalPodiums = models.IntegerField()
    totalPoints = models.IntegerField()
    totalPolePositions = models.IntegerField()
    totalFastestLaps = models.IntegerField()
    totalDriverOfTheDay = models.IntegerField()
    totalGrandSlams = models.IntegerField()

    class Meta:
        verbose_name = 'Sessions Drivers'

class sessions_drivers_standings(models.Model):
    year = models.ForeignKey(sessions, related_name='year_sessions_drivers_standings', on_delete=models.CASCADE)
    positionDisplayOrder = models.IntegerField()
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    driverID = models.ForeignKey(drivers, related_name='sessions_drivers_standings_driverID', on_delete=models.CASCADE)
    points = models.IntegerField()

    class Meta:
        verbose_name = 'Sessions Drivers Standings'

class sessions_engines_manufacturers(models.Model):
    year = models.ForeignKey(sessions, related_name='year_sessions_engines_manufacturers', on_delete=models.CASCADE)
    enginesManufacturerID = models.ForeignKey(enginesManufacturers, related_name='sessions_engines_manufacturers_enginesManufacturerID', on_delete=models.CASCADE)
    positionNumber = models.IntegerField()
    positionText = models.CharField(max_length=100)
    bestStartingGridPosition = models.IntegerField()
    bestRaceResult = models.IntegerField()
    totalRaceEntries = models.IntegerField()
    totalRaceWins = models.IntegerField()
    totalRaceLaps = models.IntegerField()
    totalPodiums = models.IntegerField()
    totalPodiumRaces = models.IntegerField()
    totalPoints = models.IntegerField()
    totalPolePositions = models.IntegerField()
    totalFastestLaps = models.IntegerField()

    class Meta:
        verbose_name = 'Sessions Engines Manufacturers'