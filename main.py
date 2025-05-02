#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Agent Financier - Application de gestion des finances personnelles
"""

import os
import sys
import logging
from datetime import datetime

# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("agent_financier.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def setup_environment():
    """Initialise l'environnement de l'application"""
    logger.info("Initialisation de l'environnement...")
    
    # Cr?ation des r?pertoires n?cessaires s'ils n'existent pas
    dirs = ['data', 'logs', 'config']
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            logger.info(f"R?pertoire cr??: {directory}")
    
    logger.info("Environnement initialis? avec succ?s")

def main():
    """Fonction principale de l'application"""
    logger.info("D?marrage de l'Agent Financier")
    
    # Initialisation de l'environnement
    setup_environment()
    
    # TODO: Initialiser l'interface utilisateur
    # TODO: Charger les donn?es utilisateur
    # TODO: D?marrer le service d'analyse financi?re
    
    logger.info("Application pr?te")
    print("Bienvenue dans l'Agent Financier!")
    print("Cette application est en cours de d?veloppement.")
    print(f"Date et heure actuelles: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Erreur critique: {str(e)}", exc_info=True)
        sys.exit(1)
