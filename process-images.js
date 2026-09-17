const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const sourceDir = './StoryMe_images';
const stylesDir = './assets/img/styles';
const pricingDir = './assets/img/pricing';

// Ensure directories exist
if (!fs.existsSync(stylesDir)) fs.mkdirSync(stylesDir, { recursive: true });
if (!fs.existsSync(pricingDir)) fs.mkdirSync(pricingDir, { recursive: true });

async function processImage(inputPath, outputPath, width = 800) {
  try {
    await sharp(inputPath)
      .resize(width, null, { withoutEnlargement: true })
      .jpeg({ quality: 85 })
      .toFile(outputPath);

    const stats = fs.statSync(outputPath);
    console.log(`✅ ${path.basename(outputPath)} (${Math.round(stats.size/1024)}KB)`);
  } catch (err) {
    console.log(`❌ ${path.basename(inputPath)}: ${err.message}`);
  }
}

async function main() {
  const files = fs.readdirSync(sourceDir);

  console.log('\n📦 Processing purchase images...');
  for (const file of files) {
    if (file.toLowerCase().includes('purchase')) {
      const slug = file.toLowerCase()
        .replace('purchase - ', '')
        .replace('purchase-', '')
        .replace('.png', '')
        .replace(/\s+/g, '-');
      await processImage(
        path.join(sourceDir, file),
        path.join(pricingDir, `${slug}.jpg`),
        600
      );
    }
  }

  console.log('\n🎨 Processing style images...');
  const styleFiles = files.filter(f =>
    f.toLowerCase().includes('style') ||
    f.toLowerCase().includes('classic') ||
    f.toLowerCase().includes('enchanted') ||
    f.toLowerCase().includes('water') ||
    f.toLowerCase().includes('lego') ||
    f.toLowerCase().includes('clay') ||
    f.toLowerCase().includes('silhouette') ||
    f.toLowerCase().includes('grey') ||
    f.toLowerCase().includes('billboard')
  );

  for (const file of styleFiles) {
    // Skip duplicates and create clean names
    let slug = file.toLowerCase()
      .replace('style-', '')
      .replace('.png', '')
      .replace(/\s+/g, '-');

    // Skip if it's a duplicate
    if (slug === 'classic-fable' && files.includes('style-classic-fable.png')) continue;
    if (slug === 'water-color' && files.includes('style-watercolour.png')) continue;
    if (slug === 'enchanted-glow' && files.includes('style-enchanted-glow.png')) continue;

    await processImage(
      path.join(sourceDir, file),
      path.join(stylesDir, `${slug}.jpg`),
      800
    );
  }

  console.log('\n🖼️ Processing hero images...');
  for (const file of files) {
    if (file.toLowerCase().includes('hero') || file.toLowerCase().includes('crew')) {
      const slug = file.toLowerCase()
        .replace('.png', '')
        .replace(/\s+/g, '-');
      await processImage(
        path.join(sourceDir, file),
        `./assets/img/${slug}.jpg`,
        1200
      );
    }
  }

  console.log('\n✅ Done!');
}

main().catch(console.error);
