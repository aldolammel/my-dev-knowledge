

DIRECTIVE: V-ELSE


    >> It's accepted for: don't expect expression.


    >> Examples:
        <div v-if="Math.random() > 0.5">
            Now you see me
        </div>
        <div v-else>
            Now you don't
        </div>


    >> Avoiding v-if and v-else:
        <span>
            {{ book.isReady ? "I'm ready" : "NOT READY YET" }}
        </span>

    
    