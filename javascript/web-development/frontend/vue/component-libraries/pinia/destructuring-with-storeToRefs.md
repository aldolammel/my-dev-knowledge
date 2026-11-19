

PINIA: DESTRUCTURING WITH STORE-TO-REFS

    Just like with the Vue 3 reactive API, we cannot destructure the resulting values when
    instantiating our store. This won't work:

    >> Bad:
        const store = useCounterStore();
        const {options, increment, totalClicks} = useCounterStore();

    >> Right:
        import {storeToRefs} from 'pinia'
        const store = useCounterStore();
        const {options, increment, totalClicks} = storeToRefs(store);




