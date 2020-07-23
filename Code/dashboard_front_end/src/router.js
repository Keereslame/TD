import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
        {
            path: '/',
            name: 'Accueil',
            component: () => import("./layout/Accueil")
        },
        {
            path: '/Calendar',
            name: 'Calendar',
            component: () => import("./layout/Calendar")
        },
        {
            path: '/Data',
            name: 'Data',
            component: () => import("./layout/Data")
        },
        {
            path: "/Insert",
            alias: "/batchs",
            name: "batchs",
            component: () => import("./components/data/BatchsList")
        },
        {
            path: "/batchs/:id",
            name: "batch-details",
            component: () => import("./components/data/Batch")
        },
        {
            path: "/add",
            name: "add",
            component: () => import("./components/data/AddBatch")
        },
        {
            path: '/Stock',
            name: 'Stock',
            component: () => import("./layout/Stock")
        },
        {
            path: '/Task',
            name: 'Task',
            component: () => import("./layout/Task")
        },
        {
            path: '/Measure',
            name: 'Measure',
            component: () => import("./layout/Measure")
        }
    ]
});
