var mongoose = require('mongoose');

var batchSchema = new mongoose.Schema({
    _id: String,
    nb_bac: Number,
    template: String,
    date_start : Date,
    nb_adult: Number,
    nb_laying_day: Number,
    reproduction_humidity_mass: Number,
    reproduction_humidity_freq: Number,
    reproduction_humidity_type: String,
    substrat_initial_mass: Number,
    substrat_add_mass: Number,
    substrat_BSG: Number,
    substrat_carrot: Number,
    substrat_apple: Number,
    substrat_pear: Number,
    substrat_other: Number,
    other_type: String,
    growth_humidity_mass: Number,
    growth_humidity_freq: Numb  er,
    growth_humidity_type: String,
    humidity_delay: Number,
    humidity_total_mass: Number,
    growth_delay: Number,
    harvest_mealworm_mass: Number,
    harvest_pupa_nb: Number,
    harvest_frass_pure: Number,
    harvest_frass_filtered: String
})

var BatchModel = mongoose.model('BatchModel', batchSchema);

module.exports = BatchModel;