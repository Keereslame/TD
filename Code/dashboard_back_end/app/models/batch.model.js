module.exports = mongoose => {
    var schema = mongoose.Schema(
            {
                name: String,
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
                growth_humidity_freq: Number,
                growth_humidity_type: String,
                humidity_delay: Number,
                humidity_total_mass: Number,
                growth_day: Number,
                harvest_mealworm_mass: Number,
                harvest_pupa_nb: Number,
                harvest_frass_pure: Number,
                harvest_frass_filtered: Number
            },
    );

    schema.method("toJSON", function() {
        const { __v, _id, ...object } = this.toObject();
        object.id = _id;
        return object;
    });

    const Batch = mongoose.model("batch", schema);
    return Batch;
};
