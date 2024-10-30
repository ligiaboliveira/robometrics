from django.urls import path
from .controllers import cargo_controller, permissao_controller, equipe_controller, usuario_controller, robo_controller, sensor_controller, pista_controller, corrida_controller

urlpatterns = [
    path('cargos/', cargo_controller.get_cargos),
    path('cargos/create/', cargo_controller.create_cargo),
    path('cargos/<int:pk>/', cargo_controller.get_cargo),
    path('cargos/<int:pk>/update/', cargo_controller.update_cargo),
    path('cargos/<int:pk>/delete/', cargo_controller.delete_cargo),

    path('permissoes/', permissao_controller.get_permissoes),
    path('permissoes/create/', permissao_controller.create_permissao),
    path('permissoes/<int:pk>/', permissao_controller.get_permissao),
    path('permissoes/<int:pk>/update/', permissao_controller.update_permissao),
    path('permissoes/<int:pk>/delete/', permissao_controller.delete_permissao),

    path('equipes/', equipe_controller.get_equipes),
    path('equipes/create/', equipe_controller.create_equipe),
    path('equipes/<int:pk>/', equipe_controller.get_equipe),
    path('equipes/<int:pk>/update/', equipe_controller.update_equipe),
    path('equipes/<int:pk>/delete/', equipe_controller.delete_equipe),

    path('usuarios/', usuario_controller.get_usuarios),
    path('usuarios/create/', usuario_controller.create_usuario),
    path('usuarios/<int:pk>/', usuario_controller.get_usuario),
    path('usuarios/<int:pk>/update/', usuario_controller.update_usuario),
    path('usuarios/<int:pk>/delete/', usuario_controller.delete_usuario),

    path('robos/', robo_controller.get_robos),
    path('robos/create/', robo_controller.create_robo),
    path('robos/<int:pk>/', robo_controller.get_robo),
    path('robos/<int:pk>/update/', robo_controller.update_robo),
    path('robos/<int:pk>/delete/', robo_controller.delete_robo),
    
    path('sensores/', sensor_controller.get_sensores),
    path('sensores/create/', sensor_controller.create_sensor),
    path('sensores/<int:pk>/', sensor_controller.get_sensor),
    path('sensores/<int:pk>/update/', sensor_controller.update_sensor),
    path('sensores/<int:pk>/delete/', sensor_controller.delete_sensor),

    path('pistas/', pista_controller.get_pistas),
    path('pistas/create/', pista_controller.create_pista),
    path('pistas/<int:pk>/', pista_controller.get_pista),
    path('pistas/<int:pk>/update/', pista_controller.update_pista),
    path('pistas/<int:pk>/delete/', pista_controller.delete_pista),

    path('corridas/', corrida_controller.get_corridas),
    path('corridas/create/', corrida_controller.create_corrida),
    path('corridas/<int:pk>/', corrida_controller.get_corrida),
    path('corridas/<int:pk>/update/', corrida_controller.update_corrida),
    path('corridas/<int:pk>/delete/', corrida_controller.delete_corrida),
]