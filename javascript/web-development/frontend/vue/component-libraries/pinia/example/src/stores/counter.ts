// TYPESCRIPT VERSION:

import { defineStore } from "pinia";

type CounterOption = "a" | "b" | "c";

interface CounterState {
  options: Record<CounterOption, number>;
}

// For asynchronous cases (step 1/2):
// Just like with Vuex, Pinia actions can also be asynchronous. Imagine a case where you make an
// HTTP request and have to wait for the response to update the state or call other actions.
const wait = (time: number = 1000): Promise<void> =>
  new Promise((resolve) => setTimeout(resolve, time));

export const useCounterStore = defineStore("counter", {
  state: (): CounterState => ({
    options: {
      a: 0,
      b: 0,
      c: 0,
    },
  }),

  actions: {
    increment(option: CounterOption): void {
      this.options[option]++;
    },

    // For asynchronous cases (step 2/2):
    // Let's create delayedIncrement to wait for a number of milliseconds before updating options:
    async delayedIncrement(option: CounterOption): Promise<void> {
      await wait();
      this.options[option]++;
    },
  },

  getters: {
    totalClicks(): number {
      return Object.values(this.options).reduce((total, current) => {
        return total + current;
      }, 0);
    },
  },
});
