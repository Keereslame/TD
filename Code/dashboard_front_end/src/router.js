import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
        {
            path: "/",
            alias: "/batchs",
            name: "batchs",
            component: () => import("./components/BatchsList")
        },
        {
            path: "/batchs/:id",
            name: "batch-details",
            component: () => import("./components/Batch")
        },
        {
            path: "/add",
            name: "add",
            component: () => import("./components/AddBatch")
        }
    ]
});
