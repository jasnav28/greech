export const GAZETTE = '16th February, 2026 S.O. 876(E)';

export const PRODUCTS = [
  { 
    brand: 'BLACK DIAMOND', 
    specification: 'Potassium Humate 49% (Powder)', 
    category: 'Humic Acid and Fulvic Acid  and their Derivatives',
    crops: ['Paddy', 'Tomato'], 
    dosage: ['Paddy One soil application at 1kg/ha', 'Tomato One soil application at 1kg/ha'], 
    gazette: '16th February, 2026 S.O. 876(E)', 
    composition: [
      '(i) Potassium humate (Source: Leonardite) per cent. by weight, minimum 49', 
      '(ii) Silwet power (adjuvant) per cent. by weight, maximum 0.5',
      '(iii) Carboxymethyl cellulose per cent. by weight, maximum 1.0',
      '(iv) Maltodextrin powder per cent. by weight QS',
      '(v) Total (per cent.) 100'
    ] 
  },
];

export const SLUG_TO_BRAND = {
  'BLACK DIAMOND': 'BLACK DIAMOND',
  'BLACK%20DIAMOND': 'BLACK DIAMOND',
  'black diamond': 'BLACK DIAMOND',
  'BLACKDIAMOND': 'BLACK DIAMOND',
  'blackdiamond': 'BLACK DIAMOND',
};

export function findProductBySlug(slug) {
  const decoded = decodeURIComponent(slug);
  const normalized = decoded.replace(/\+/g, ' ');
  const brand = SLUG_TO_BRAND[normalized] || SLUG_TO_BRAND[slug] || normalized;
  const found = PRODUCTS.find(p => p.brand.toUpperCase() === brand.toUpperCase());
  return found || PRODUCTS[0];
}

export function findProductByBrand(brand) {
  return PRODUCTS.find(p => p.brand === brand) || PRODUCTS[0];
}
