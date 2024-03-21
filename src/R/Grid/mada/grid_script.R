

#put the name of the desired country

country <- "Madagascar"
#put the start year, end year and the estimation interval 
years   <- seq(2000, 2020, by = 5)


## Import World Shapefile ----

world <- rnaturalearth::ne_countries(scale = "large", returnclass = "sf")


## Select Madagascar boundaries ----

region_shp <- world[world$admin == country, ]


## Create raster ----
# 1 degree ~ 100 km

grille <- raster::raster(region_shp, res = 1 / 20) # Resolution ~ 5 km

## Add values (all cells are equal to 1) ----

grille[] <- 1


## Mask cells outside Madagascar ----

grille <- raster::mask(grille, region_shp)


## Identify cells with values (!= NA) ----

non_na_cells <- which(!is.na(grille[]))


## Get non-NA cells center coordinates ----

mada_xy <- raster::xyFromCell(grille, non_na_cells)
mada_xy <- as.data.frame(mada_xy)


## Plot to check ----

plot(mada_xy[ , c("x", "y")], asp = 1, main = country)


## Add year column + Export to csv ----

for (year in years) {
  
  mada_xy$"year" <- year
  
  write.csv(mada_xy, here::here("outputs", paste0(tolower(country), "_latlon_",
                                                  year, ".csv")), 
            row.names = FALSE)
}
