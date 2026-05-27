

BIOS: HOW TO TURN ON AND OFF THE 'SECURE BOOT'


    This will avoid many issues during any OS installation, specially those OS using custom configs.
    The entire Secure Boot roadmap below might change a few BIOS areas based in your motherboard, but the logic will prevail.

    E.g. using a Gigabyte B450 AORUS M with bios version F67 (feb/2026):

    
    A) "I WILL START THE SYSTEM FORMATTING" - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        A.1) Acessar a BIOS - Reinicie o seu computador e pressione a tecla Delete repetidamente assim que o computador for ligar para entrar na configuração da BIOS.

        A.2) Navegar até o Menu "Boot" - Dentro da BIOS, procure e selecione a aba Boot  (Inicializar). Geralmente, ela fica na parte superior da tela.

        A.3) Desabilitar o CSM (Compatibility Support Module) - Localize a opção CSM Support e mude o status dela para Disabled (Desabilitado) . Esta é a etapa mais importante. O Secure Boot só fica visível e pode ser ativado quando o CSM está desligado.

            IMPORTANT:
                Após desabilitar o CSM, a BIOS pode pedir para salvar e reiniciar antes de prosseguir.

        A.4) Localizar o Menu "Secure Boot" - Ainda na aba Boot, após desabilitar o CSM, a opção Secure Boot deve aparecer. Selecione-a para entrar no submenu de configurações.

        A.5) Configurar o Secure Boot - Dentro do menu Secure Boot, siga esta sequência com cuidado:
        Mude o "Secure Boot Mode" (Modo de Inicialização Segura) de Standard (Padrão) para Custom (Personalizado). Isso desbloqueará as opções abaixo.
        
        Com o modo "Custom" ativo, a opção Restore Factory Keys (Restaurar Chaves de Fábrica) ficará disponível. Selecione-a e confirme Yes (Sim) para carregar as chaves seguras, incluindo as da Microsoft .

        Após restaurar as chaves, o sistema provavelmente exibirá uma mensagem para reiniciar ("Reset Without Saving"). Confirme Yes novamente. O computador será reiniciado para aplicar as chaves.

        A.6) Ativar o Secure Boot - Após a reinicialização, entre na BIOS mais uma vez. Volte ao menu Boot > Secure Boot. Agora você verá que a opção principal Secure Boot (ou o status dela) poderá ser alterada. Mude-a para Enabled (Ativado) . O status final correto deve ser algo como "Active" (Ativo) e o "System Mode" (Modo do Sistema) como "User" (Usuário).

        A.7) Salvar e Sair - Vá até a aba Save & Exit (Salvar e Sair) e selecione Save Changes and Reset (Salvar Alterações e Reiniciar).



    B) "I HAVE FINISHED THE SYSTEM FORMATTING" - - - - - - - - - - - - - - - - - - - - - - - - - - -

        IMPORTANT:
            If you will install more than one OS, first install all of them before to proceed with the CSM re-activation!

        B.1) In BIOS, go to 'BIOS' but, before to turn ON the CSM, first get in Secure Boot configurations and turn it manually OFF!

        B.2) Once that's done, finally, turn ON the CSM, and make sure its configurations below are using "UEFI Only".

        B.3) (If applicable) Re-check your boot devices' order, putting the Ubuntu and other possible OS devices in the order of priority for boot. 

        B.4) Save it and reboot. Done!



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

