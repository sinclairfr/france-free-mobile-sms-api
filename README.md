Petit script python pour utiliser le service "notification par sms" de Free Mobile SAS

## Avant utilisation

Éditez le script en renseignant les champs user et pass avec vos propres identifiants.
```
- user : votre login

- pass : votre clé d’identification générée automatiquement par notre service
```

Le resultat devrait ressembler à cela :

```
# user : votre identifiant freemobile, du type 11111111
user = 1111111
# pass : votre clé d’identification générée automatiquement par notre service
pass = AAAAAAAAAAAAAAA
```

### Utilisation

Dans un shell, executer :

```
python freemobile_send_sms.py 'votre message ici'
```

Attention : utiliser les guillemets simples pour passer l'argument message.

### Pre-requis

Le service doit être activé dans l’espace abonné de freemobile.fr

Avoir python installé sur votre système.

### Resultat

Si vous ne recevez pas de message d'erreur dans le shell, le message devrait avoir été correctement envoyé.

## Auteur

* **Mehdi FEKIH** 

## License

MIT License - Libre de droit. 
