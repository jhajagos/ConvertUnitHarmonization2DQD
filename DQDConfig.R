checkNames <- c("plausibleValueLow", "plausibleValueHigh")
outputFile <- "hi_unite_harmonization_results.json"
writeToTable <- FALSE

conceptCheckThresholdLoc <- "/home/rstudio/s1_s2_merged.csv"

DataQualityDashboard::executeDqChecks(connectionDetails = connection,
                                    cdmDatabaseSchema = cdmDatabaseSchema,
                                    resultsDatabaseSchema = resultsDatabaseSchema,
                                    cdmSourceName = cdmSourceName,
                                    numThreads = numThreads,
                                    sqlOnly = sqlOnly,
                                    outputFolder = outputFolder,
                                    outputFile = outputFile,
                                    verboseMode = verboseMode,
                                    writeToTable = writeToTable,
                                    checkLevels = checkLevels,
                                    tablesToExclude = tablesToExclude,
                                    cdmVersion = "5.3.1",
                                    checkNames = checkNames,
                                    conceptCheckThresholdLoc = conceptCheckThresholdLoc
)