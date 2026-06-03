

CREATING A NEW COMPONENT (DEDICATED FILES):


    0) Basic about it:
        ./5-components.txt


    1) Make sure you got the folder:
        /vue_project_root/src/components/

        >> Organizing even more:
            /components/pages/  = those comps that you consider main pages of Vue, like Home.vue;
            /components/layout/ = those comps used basically through all pages like NavMainMenu.vue;
            /components/common/ = those comps that compose a page but is not a layout component.


    2) In /components/ create the component file:
        MyComponentName.vue

            # Its content:
            <script setup>  <!-- SETUP only in case you're using 'Composition API' approach -->
            // code...
            </script>

            <template>
                <div>
                    My New Component
                </div>
            </template>

            <!-- Not mandatory: -->
            <style>
            </style>


    3) Import the component in its parent-component (App.vue, for example):

        <script setup>  <!-- SETUP only in case you're using 'Composition API' approach -->
        // Importing the child-component in its parent:
        import MyComponentName from './components/MyComponentName.vue';
        
        //...
        
        // Applying the new child-component:
        <MyComponentName />

        //...
        </script>


    4) If you need to call external data (from App.vue, for example), you must to use PROPS in
        your component file:
            ./5.1-props.txt

