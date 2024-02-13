db.birds.insertMany([
  {
    name: "Bald Eagle",
    scientificName: "Haliaeetus leucocephalus",
    habitat: "Forests, lakes, rivers, coasts",
    diet: ["Fish", "Small mammals", "Waterfowl"],
    conservationStatus: "Least Concern",
    lifespan: 20, // in years
    wingspan: 6.6, // in feet
    imageUrl: "https://example.com/bald_eagle.jpg",
    description: "The bald eagle is a bird of prey found in North America...",
    relatedSpecies: ["Golden Eagle", "White-tailed Eagle"],
  },
  {
    name: "Mallard",
    scientificName: "Anas platyrhynchos",
    habitat: "Lakes, ponds, marshes",
    diet: ["Aquatic plants", "Insects", "Small fish"],
    conservationStatus: "Least Concern",
    lifespan: 5, // in years
    wingspan: 2.1, // in feet
    imageUrl: "https://example.com/mallard.jpg",
    description:
      "The mallard is a dabbling duck that breeds throughout the temperate and subtropical Americas...",
    relatedSpecies: ["Northern Pintail", "Gadwall"],
  },
  {
    name: "Peregrine Falcon",
    scientificName: "Falco peregrinus",
    habitat: "Cliffs, tall buildings, open country",
    diet: ["Birds", "Small mammals"],
    conservationStatus: "Least Concern",
    lifespan: 15, // in years
    wingspan: 3.4, // in feet
    imageUrl: "https://example.com/peregrine_falcon.jpg",
    description: "The peregrine falcon is a widespread bird of prey...",
    relatedSpecies: ["Gyrfalcon", "Prairie Falcon"],
  },
]);
