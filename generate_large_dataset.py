import pandas as pd
import random
import string
from faker import Faker

fake = Faker()
random.seed(42)  # Para resultados reproducibles

def generate_business_contacts(count=7000):
    """
    Genera un dataset de contactos profesionales con duplicados intencionales
    y errores comunes para demostrar el impacto del limpiador.
    """
    
    print(f"🚀 Generando {count} contactos de demostración...")
    
    contacts = []
    
    # Tipos de empresas para hacer más realista
    company_types = ['Corp', 'Inc', 'LLC', 'Ltd', 'Group', 'Solutions', 'Systems', 'Technologies', 'Services']
    
    for i in range(count):
        # Generar datos base
        first_name = fake.first_name()
        last_name = fake.last_name()
        
        # Simular algunos errores comunes en emails
        if random.random() < 0.05:  # 5% emails inválidos
            email = f"{first_name.lower()}@invalid-domain"
        elif random.random() < 0.03:  # 3% emails con errores
            email = f"{first_name.lower()}..{last_name.lower()}@{fake.domain_name()}"
        else:
            email = f"{first_name.lower()}.{last_name.lower()}@{fake.domain_name()}"
        
        # Generar teléfonos con formatos inconsistentes
        phone_base = fake.phone_number()
        if random.random() < 0.3:  # 30% teléfonos mal formateados
            phone = phone_base.replace('(', '').replace(')', '').replace('-', ' ')
        elif random.random() < 0.2:  # 20% con puntos
            phone = phone_base.replace('-', '.')
        else:
            phone = phone_base
        
        # Generar empresa
        company_name = fake.company()
        if random.random() < 0.5:
            company = f"{company_name} {random.choice(company_types)}"
        else:
            company = company_name
        
        contact = {
            'name': f"{first_name} {last_name}",
            'email': email,
            'phone': phone,
            'company': company
        }
        
        contacts.append(contact)
        
        # Progreso cada 1000 contactos
        if (i + 1) % 1000 == 0:
            print(f"📊 Generados {i + 1} contactos...")
    
    # Crear DataFrame
    df = pd.DataFrame(contacts)
    
    # Agregar duplicados intencionales (10% del total)
    duplicates_count = int(count * 0.1)
    print(f"🔄 Agregando {duplicates_count} duplicados intencionales...")
    
    duplicate_indices = random.sample(range(len(df)), duplicates_count)
    duplicates = df.iloc[duplicate_indices].copy()
    
    # Modificar ligeramente algunos duplicados para simular errores reales
    for idx in range(len(duplicates)):
        if random.random() < 0.5:
            # Cambiar formato del teléfono manteniendo el mismo número
            duplicates.iloc[idx]['phone'] = duplicates.iloc[idx]['phone'].replace('(', '').replace(')', '').replace('-', ' ')
        if random.random() < 0.3:
            # Agregar espacios o puntos extra en email
            email = duplicates.iloc[idx]['email']
            duplicates.iloc[idx]['email'] = email.replace('@', ' @').replace('.', ' .')
    
    # Combinar datos originales con duplicados
    df_final = pd.concat([df, duplicates], ignore_index=True)
    
    # Mezclar el dataset
    df_final = df_final.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return df_final

def main():
    """Generar dataset grande y guardarlo"""
    print("🎯 Generando dataset de 7,000 contactos para demostración...")
    
    try:
        # Generar dataset
        df = generate_business_contacts(7000)
        
        # Guardar archivo
        output_file = 'large_business_contacts.csv'
        df.to_csv(output_file, index=False)
        
        print(f"\n✅ Dataset generado exitosamente!")
        print(f"📁 Archivo: {output_file}")
        print(f"📊 Total de contactos: {len(df)}")
        print(f"🔄 Duplicados incluidos: ~{int(len(df) * 0.1)}")
        print(f"⚠️  Emails inválidos: ~{int(len(df) * 0.08)}")
        print(f"📱 Teléfonos mal formateados: ~{int(len(df) * 0.5)}")
        
        # Mostrar muestra
        print(f"\n📋 Muestra de los primeros 5 contactos:")
        print(df.head().to_string(index=False))
        
    except Exception as e:
        print(f"❌ Error generando dataset: {str(e)}")

if __name__ == "__main__":
    main()