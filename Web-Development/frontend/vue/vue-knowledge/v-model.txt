

DIRECTIVE: V-MODEL
    
    >> Create a two-way binding on a form input element or a component.

    >> It's accepted for: varies based on value of form inputs element or output of components!

    >> Example:

        >> You got a Quiz where each question has answers as options to select. Then you want to
            store the chosen answer:
        
            # On <script> layer:
                
                // Using the 'options-api' as scripting approach:
                export default {
                    data() {
                        return {
                            chosenAnswer: undefined,
                        }
                    },
                    //...
                }

                // Or using the 'composition-api' as scripting approach:
                xxxxxxxxxxx
                xxxxxxxxxxxx
                xxxxxxxxxxxxxxxxxxxxx

            # On <template> layer:
                
                <input
                    :id="`q${idx}`"
                    v-model="chosenAnswer"
                    type="radio"
                    name="options"
                    :value="answer"
                >
    
    
    
    >> HOW TO XXXXXXXXXXXXXXXXXXXXXXXXX:

        xxxxxxxxxxxxxxxxxxxxxxx