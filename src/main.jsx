import React, { useEffect, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import {
  ArrowDown,
  ArrowLeft,
  ArrowRight,
  ArrowUpRight,
  CalendarDays,
  Check,
  ChevronDown,
  Clock3,
  Facebook,
  Instagram,
  Mail,
  MapPin,
  Menu,
  MessageCircle,
  Phone,
  Play,
  Quote,
  Scissors,
  Sparkles,
  Star,
  X,
} from 'lucide-react';
import './styles.css';

const phoneDisplay = '+254 795 216 012';
const whatsappHref = 'https://wa.me/254795216012?text=Hello%20Nyota%20Swerve%2C%20I%20would%20like%20to%20book%20a%20consultation.';
const mapsHref = 'https://www.google.com/maps/place/Nyota.+Swerve.+Closet/@-1.1338507,36.9744499,3a,75y,90t/data=!3m8!1e2!3m6!1sCIABIhB6eDCFhRYBpItwMv8U_QG_!2e10!3e12!6shttps:%2F%2Flh3.googleusercontent.com%2Fgps-cs-s%2FAHRPTWn6iXRsdloNiPFsUbv2C3FaRQp3PPwbd7KY1pSTgGdxxVlmAOPThu4AbS7ssnZl4iqK2aJjeHFkTQh52phYyQy-71AU_he3dYXWF4-89JlHpnmaCTExbK52Er3fMuIuhpeBL2zdO-IfRCA%3Dw203-h101-k-no!7i11811!8i5906!4m9!3m8!1s0x182f4748a6a9a321:0xdc1e2f82dccb9930!8m2!3d-1.1338746!4d36.9743651!10e5!14m1!1BCgIgAQ!16s%2Fg%2F11njcycps5';

// Owner-uploaded photos from the Nyota Swerve Google Maps listing.
const mapsImages = [
  'https://lh3.googleusercontent.com/gps-cs/AH1DqX_u8oD6ehnEBP4uXbuPmAWhb7JQQTYnUG5YZtl_gup2gs700hYgvxW-iMJ1KEdZEtfO_BhckhiMZH9tVPwT0LquEi6Qne-x7zehDNPrS0_Vk0-uueDe1UvkaVXt91GsdpYYKnLXRVCiOMBe=w1200-h1600-p-k-no',
  'https://lh3.googleusercontent.com/gps-cs/AH1DqX_EKu9-0S37jHY96PwLpwbdfHmPc1SWy2JX8iCRxMLT0nyKyvp_Id4BYZ3Qr4BEOn2DLElXbjNXQZT30M1QXh0bXvGcGPuxnkenY_A4rZ80qW8pRukNlzLcnBsACRUaHQzdjaJYCYRI1B0=w1200-h1600-p-k-no',
  'https://lh3.googleusercontent.com/gps-cs/AH1DqX9YVcROV6ALOifK37yeqk7ni4A4vBmi5ZZKe6tvDNsgZGdZGEICsd_bItsx4ZJbi-q10KGmGDHn5IityR_2RcrdEeva6-6rtE-fbuid8am0ulqnTLTgTJJbL4IW2P_BcqUa2lsshzYyDnWF=w1200-h1600-p-k-no',
  'https://lh3.googleusercontent.com/gps-cs/AH1DqX_vyJzHf1MWYwP6WgkEupRy8qpXT3fvIhVM4bgZ96DDrTqFWWjBPbvagI1zsniY_kJX8Q2cG2gC3WpPGp-7lxHDD1Se5YailkX6xu8ANS3jDEvWm3CoN9tyKlv_VXUguQZVxX3AfpPtgV6G=w1200-h1600-p-k-no',
  'https://lh3.googleusercontent.com/gps-cs/AH1DqX-TgFWzto2LU15X2kgkrUym2lCDg-XJapOYInYYAFTLhjQrgMht5ZnOLACeiIMd27rnYF2Jtf1GiS3pPOjGm_pB_Ci3Ofi_XsFk-v0erryuXx9Yp76QobTYodD7DAh5om2mExx7tlpkIs5m=w1200-h1600-p-k-no',
  'https://lh3.googleusercontent.com/gps-cs/AH1DqX9Gjcfppb92Az7jLuilOq-I6Q6kcK_5CPj8XCafmAtatMg09w4F3e2ZQzeDYVwixMQcL5ngx8eYpmJ1WTKzM7HB5ihXYCerGiDoeerZoA8S0-lKMHjIkwOAqbxtdP6lobBaLKjgfG4kfWvL=w1200-h1600-p-k-no',
  'https://lh3.googleusercontent.com/gps-cs/AH1DqX8TlRe953-H1shifk1S0Mc4o16QMelE0VCz_pWFsWFYGmNdYDVNPGV3EbtvQeUZ_BUNXtwm1vMuh4RdBQmb3tobayCaPTvH7vgrsXWop0wiACEcmHVj0kHhFHEODLhhjhhKgDZCatScrBE=w1200-h1600-p-k-no',
  'https://lh3.googleusercontent.com/gps-cs/AH1DqX9M7BeXgEmewFwdrCbvTGfWQimKuybpO_Ab5oAwnGg37IGy_NjSopJi_gfRoVW9-YFq7KXXVq9MGGgbEkUMHFDODYSjaTmNhDinq7Semus5OJDemLyPbQYRu39mK5KiGIgw_ynbc6S6hWo=w1200-h1600-p-k-no',
  'https://lh3.googleusercontent.com/gps-cs/AH1DqX-KlaqkF636_qv_zYT8el4eJHOc_pVnToAZXvQK8LKX8F0E_P12uJmhb9KxcmnwYGkQVwajIdcHgJQUvIalW7K4kF3NIU5XLf_Rk_y4FHdLJucQ-eNoSfzM3gk-JUsofR8pP6VulkiWkXg3=w1200-h1600-p-k-no',
  'https://lh3.googleusercontent.com/gps-cs/AH1DqX9Xjow5SCIHyOYGPGKH2rxk9GSR6QnlKQ64kCeDpaL1jXuwHEkW3EIci5ewgbMbru3Gj3XuzGFUFVgMkIHUqop6mKS4OpwNvD8FPoq-6wcG-YEYNlvWcG6i1mynvIyaM04TsJCA2muYb5w=w1200-h1600-p-k-no',
];

const services = [
  {
    number: '01',
    title: 'Bespoke tailoring',
    copy: 'One pattern, cut only for you. From business suits to statement tuxedos, every detail follows your frame and your story.',
    image: mapsImages[9],
    items: ['Two & three-piece suits', 'Tuxedos & dinner jackets', 'Blazers, trousers & shirts'],
  },
  {
    number: '02',
    title: 'Wedding atelier',
    copy: 'A composed wedding wardrobe for the groom and his circle, designed to feel connected without ever looking uniform.',
    image: mapsImages[4],
    items: ['Groom consultation', 'Groomsmen packages', 'Finishing accessories'],
  },
  {
    number: '03',
    title: 'Corporate & care',
    copy: 'Confident tailoring for teams, plus expert alterations that restore proportion, comfort and polish to the clothes you own.',
    image: mapsImages[3],
    items: ['Corporate wardrobes', 'Jacket & trouser resizing', 'Repairs and alterations'],
  },
];

const process = [
  { step: '01', title: 'The conversation', text: 'We learn your occasion, style and the impression you want to make.' },
  { step: '02', title: 'Cloth & character', text: 'Explore fabrics, colours, silhouettes and considered design details.' },
  { step: '03', title: 'Your measurement', text: 'Precise body measurements create the foundation for an exact fit.' },
  { step: '04', title: 'The making', text: 'Our atelier cuts, constructs and refines your garment by hand.' },
  { step: '05', title: 'Final fitting', text: 'We perfect the balance, perform quality checks and prepare delivery.' },
];

const gallery = [
  { src: mapsImages[0], title: 'Signature pinstripe', category: 'Bespoke', source: 'Nyota Swerve', tall: true },
  { src: mapsImages[1], title: 'Corporate confidence', category: 'Corporate', source: 'Nyota Swerve', tall: true },
  { src: mapsImages[2], title: 'A wedding with character', category: 'Wedding', source: 'Nyota Swerve', tall: true },
  { src: mapsImages[3], title: 'Tailored in blue', category: 'Corporate', source: 'Nyota Swerve', tall: true },
  { src: mapsImages[4], title: 'The Nyota signature', category: 'Brand', source: 'Nyota Swerve' },
  { src: mapsImages[5], title: 'The pinstripe edit', category: 'Fabrics', source: 'Nyota Swerve', tall: true },
  { src: mapsImages[6], title: 'Cloth selection', category: 'Fabrics', source: 'Nyota Swerve', tall: true },
  { src: mapsImages[7], title: 'The stripe collection', category: 'Fabrics', source: 'Nyota Swerve', tall: true },
  { src: mapsImages[8], title: 'The maker at work', category: 'Atelier', source: 'Nyota Swerve', tall: true },
  { src: mapsImages[9], title: 'Colour, cut, character', category: 'Bespoke', source: 'Nyota Swerve', tall: true },
];

const homepageGallery = [gallery[1], gallery[5], gallery[6], gallery[7]];

const journal = [
  {
    category: 'The fit guide',
    date: '6 min read',
    title: 'How should a suit really fit?',
    copy: 'The quiet details—from shoulder line to trouser break—that separate a good suit from a great one.',
  },
  {
    category: 'Wedding notes',
    date: '4 min read',
    title: 'A groom’s guide to black tie',
    copy: 'Peak or shawl lapel? Bow tie or necktie? Start with the codes, then make the look your own.',
  },
  {
    category: 'Cloth stories',
    date: '5 min read',
    title: 'Choosing fabric for Kenya’s climate',
    copy: 'A practical look at weight, weave and breathability for an elegant suit that stays comfortable.',
  },
];

const testimonials = [
  {
    quote: 'From the first consultation to the final fitting, I felt completely looked after. The suit moved beautifully and felt like me—only sharper.',
    name: 'Samuel K.',
    role: 'Wedding client',
  },
  {
    quote: 'Nyota understood the balance we needed: a consistent executive look without losing each person’s character. Every detail was considered.',
    name: 'Dennis M.',
    role: 'Corporate client',
  },
  {
    quote: 'I had four days before an important event. The fit, the finish and the service were all exceptional. I walked in with total confidence.',
    name: 'Brian N.',
    role: 'Bespoke client',
  },
];

function Brand({ compact = false, homeHref = '#top' }) {
  return (
    <a className={`brand ${compact ? 'brand--compact' : ''}`} href={homeHref} aria-label="Nyota Swerve home">
      <svg className="brand__mark" viewBox="0 0 44 44" aria-hidden="true">
        <path d="M22 2.8l2.8 14.4L39 20.4l-14.2 3.2L22 41.2l-2.8-17.6L5 20.4l14.2-3.2L22 2.8Z" />
        <circle cx="22" cy="20.5" r="2.4" />
      </svg>
      <span className="brand__words"><strong>NYOTA</strong><em>SWERVE</em></span>
    </a>
  );
}

function Header({ onBook, innerPage = false }) {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  useEffect(() => {
    document.body.classList.toggle('menu-open', open);
    return () => document.body.classList.remove('menu-open');
  }, [open]);

  const close = () => setOpen(false);

  return (
    <>
      <div className="top-note">
        <span>Ruiru, Kenya</span>
        <span className="top-note__centre"><Sparkles size={12} /> Typical turnaround in 4 days</span>
        <a href={whatsappHref} target="_blank" rel="noreferrer">WhatsApp us <ArrowUpRight size={13} /></a>
      </div>
      <header className={`site-header ${scrolled ? 'site-header--scrolled' : ''}`}>
        <Brand homeHref={innerPage ? '/' : '#top'} />
        <nav className="desktop-nav" aria-label="Primary navigation">
          <a href={innerPage ? '/#story' : '#story'}>Our story</a>
          <a href={innerPage ? '/#services' : '#services'}>Services</a>
          <a href={innerPage ? '/#weddings' : '#weddings'}>Weddings</a>
          <a href="/gallery">Gallery</a>
          <a href={innerPage ? '/#journal' : '#journal'}>Journal</a>
        </nav>
        <div className="header-actions">
          <button className="text-button desktop-book" onClick={onBook}>Book a fitting <ArrowUpRight size={15} /></button>
          <button className="menu-button" onClick={() => setOpen(!open)} aria-expanded={open} aria-label="Toggle menu">
            {open ? <X /> : <Menu />}
          </button>
        </div>
      </header>
      <div className={`mobile-menu ${open ? 'is-open' : ''}`} aria-hidden={!open}>
        <nav aria-label="Mobile navigation">
          {[
            ['Our story', innerPage ? '/#story' : '#story'],
            ['Services', innerPage ? '/#services' : '#services'],
            ['Weddings', innerPage ? '/#weddings' : '#weddings'],
            ['Gallery', '/gallery'],
            ['Journal', innerPage ? '/#journal' : '#journal'],
            ['Contact', innerPage ? '/#contact' : '#contact'],
          ].map(([label, href], i) => (
            <a key={href} href={href} onClick={close}><span>0{i + 1}</span>{label}<ArrowUpRight /></a>
          ))}
        </nav>
        <div className="mobile-menu__footer">
          <p>Ready when you are.</p>
          <button className="button button--gold" onClick={() => { close(); onBook(); }}>Book a consultation</button>
        </div>
      </div>
    </>
  );
}

function Hero({ onBook }) {
  return (
    <main id="top">
      <section className="hero">
        <div className="hero__image" style={{ '--hero-image': `url("${mapsImages[0]}")` }} role="img" aria-label="A Nyota Swerve client in a bespoke pinstripe suit" />
        <div className="hero__shade" />
        <div className="hero__content shell">
          <h1>Impeccably<br />tailored.<br /><em>Unmistakably yours.</em></h1>
          <p>Precision-made suits for men who understand that presence begins before a word is spoken.</p>
          <div className="hero__actions">
            <button className="button button--gold" onClick={onBook}>Begin your suit <ArrowUpRight size={17} /></button>
            <a className="button button--ghost" href="#services">Explore the atelier</a>
          </div>
        </div>
        <div className="hero__meta">
          <span>Est. in Kenya</span><i />
          <span>Cut to your measure</span><i />
          <span>Made in 4 days*</span>
        </div>
        <a className="hero__scroll" href="#story" aria-label="Scroll to our story"><ArrowDown /></a>
      </section>
    </main>
  );
}

function Story() {
  return (
    <section className="story section shell" id="story">
      <div className="story__aside reveal">
        <div className="eyebrow"><span /> Our house</div>
        <p className="story__index">01 / 06</p>
      </div>
      <div className="story__main reveal">
        <h2>We do not simply make suits.<br /><em>We shape confidence.</em></h2>
        <div className="story__copy-grid">
          <p className="lead">Nyota Swerve is a Kenyan bespoke tailoring house built on a simple belief: every man deserves clothing that honours his individuality.</p>
          <div>
            <p>We combine exacting measurement, premium cloth and modern African sensibility to create garments with presence. Every piece is considered from first conversation to final stitch.</p>
            <a className="underlink" href="#process">Discover our process <ArrowRight size={15} /></a>
          </div>
        </div>
      </div>
      <div className="story__signature" aria-hidden="true">NS</div>
    </section>
  );
}

function ServiceCard({ service }) {
  return (
    <article className="service-card reveal">
      <div className="service-card__image">
        <img src={service.image} alt="" loading="lazy" referrerPolicy="no-referrer" />
        <span>{service.number}</span>
      </div>
      <div className="service-card__body">
        <h3>{service.title}</h3>
        <p>{service.copy}</p>
        <ul>{service.items.map(item => <li key={item}><Check size={14} />{item}</li>)}</ul>
        <a href="#booking">Explore service <ArrowUpRight size={15} /></a>
      </div>
    </article>
  );
}

function Services() {
  return (
    <section className="services section" id="services">
      <div className="shell">
        <div className="section-head reveal">
          <div><div className="eyebrow eyebrow--light"><span /> What we create</div><p>02 / 06</p></div>
          <h2>A wardrobe, made<br /><em>around you.</em></h2>
          <p>From the room where you say “I do” to the room where decisions are made—we tailor for every defining moment.</p>
        </div>
        <div className="services-grid">
          {services.map(service => <ServiceCard service={service} key={service.title} />)}
        </div>
        <div className="service-marquee" aria-hidden="true">
          <div>SUITS <Star /> TUXEDOS <Star /> SHIRTS <Star /> OVERCOATS <Star /> ALTERATIONS <Star /> ACCESSORIES <Star /> SUITS <Star /> TUXEDOS <Star /></div>
        </div>
      </div>
    </section>
  );
}

function Wedding({ onBook }) {
  return (
    <section className="wedding" id="weddings">
      <div className="wedding__image reveal"><img src={mapsImages[2]} alt="Nyota Swerve wedding party in coordinated tailoring" loading="lazy" referrerPolicy="no-referrer" /></div>
      <div className="wedding__copy reveal">
        <div className="eyebrow"><span /> The wedding atelier</div>
        <h2>Your day.<br />Your people.<br /><em>Your signature.</em></h2>
        <p>From one exceptional tuxedo to a perfectly coordinated wedding party, we make sure every man arrives with confidence.</p>
        <div className="wedding__features">
          <span><b>01</b> Private style consultation</span>
          <span><b>02</b> Groom & groomsmen fittings</span>
          <span><b>03</b> Accessories & final styling</span>
          <span><b>04</b> Priority wedding timelines</span>
        </div>
        <button className="button button--dark" onClick={onBook}>Plan your wedding look <ArrowUpRight size={17} /></button>
      </div>
    </section>
  );
}

function Process() {
  return (
    <section className="process section" id="process">
      <div className="shell">
        <div className="section-head section-head--dark reveal">
          <div><div className="eyebrow"><span /> The Nyota way</div><p>03 / 06</p></div>
          <h2>From first word<br /><em>to final stitch.</em></h2>
          <div className="turnaround"><Clock3 /><span><b>4 days</b>Typical turnaround*</span></div>
        </div>
        <div className="process-grid">
          {process.map((item, index) => (
            <article className="process-card reveal" key={item.step} style={{ '--delay': `${index * 70}ms` }}>
              <span>{item.step}</span>
              <div className="process-card__line"><i /></div>
              <h3>{item.title}</h3>
              <p>{item.text}</p>
            </article>
          ))}
        </div>
        <div className="process-note">
          <Scissors size={18} /><p>*Turnaround can vary by garment, quantity and fabric availability. We confirm your timeline at consultation.</p>
        </div>
      </div>
    </section>
  );
}

function Gallery({ full = false }) {
  const [filter, setFilter] = useState('All');
  const [active, setActive] = useState(null);
  const categories = ['All', 'Bespoke', 'Wedding', 'Corporate', 'Fabrics', 'Atelier', 'Brand'];
  const collection = full ? gallery : homepageGallery;
  const shown = filter === 'All' ? collection : collection.filter(item => item.category === filter);

  useEffect(() => {
    const close = e => e.key === 'Escape' && setActive(null);
    window.addEventListener('keydown', close);
    return () => window.removeEventListener('keydown', close);
  }, []);

  return (
    <section className={`gallery section ${full ? 'gallery--full' : 'gallery--preview'}`} id={full ? 'portfolio' : 'gallery'}>
      <div className="shell">
        <div className="gallery__head reveal">
          <div><div className="eyebrow"><span /> {full ? 'The full collection' : 'Gallery'}</div><p>{full ? `${gallery.length} stories` : '04 / 06'}</p></div>
          <h2>{full ? <>Explore the work.<br /><em>Find your direction.</em></> : <>A glimpse of<br /><em>the Nyota life.</em></>}</h2>
          {full ? (
            <p className="gallery__intro">Wedding tailoring, sharp business wear, black tie and the craft behind every finished piece.</p>
          ) : (
            <p className="gallery__intro">Weddings, fittings, transformations and clients wearing their finished pieces with confidence.</p>
          )}
        </div>
        {full && (
          <div className="gallery-toolbar reveal">
            <div className="filters" role="group" aria-label="Filter gallery">
              {categories.map(category => (
                <button className={filter === category ? 'active' : ''} onClick={() => setFilter(category)} key={category}>{category}</button>
              ))}
            </div>
            <div className="gallery-toolbar__meta">
              <span>{String(shown.length).padStart(2, '0')} images</span>
              <a href={mapsHref} target="_blank" rel="noreferrer">Google Maps photos <ArrowUpRight size={13} /></a>
            </div>
          </div>
        )}
        <div className={`gallery-grid ${shown.length < 3 ? 'gallery-grid--small' : ''} ${full ? 'gallery-grid--full' : 'gallery-grid--preview'}`}>
          {shown.map((item, index) => (
            <button className={`gallery-item ${full && item.tall ? 'gallery-item--tall' : ''} ${full && item.wide ? 'gallery-item--wide' : ''} ${active?.src === item.src ? 'gallery-item--active' : ''}`} key={item.src} onClick={() => setActive(item)} aria-label={`View ${item.title}`}>
              <img src={item.src} alt={item.title} loading="lazy" referrerPolicy="no-referrer" onError={item.fallback ? e => { e.currentTarget.onerror = null; e.currentTarget.src = item.fallback; } : undefined} />
              <span className="gallery-item__number">{String(index + 1).padStart(2, '0')}</span>
              <span className="gallery-item__caption"><small>{item.source ? `${item.category} · ${item.source}` : item.category}</small><strong>{item.title}</strong></span>
              <span className="gallery-item__view"><ArrowUpRight /></span>
            </button>
          ))}
        </div>
        {!full && (
          <div className="gallery__more reveal">
            <p>There is more to see.</p>
            <a className="button button--gold" href="/gallery">View the full gallery <ArrowUpRight size={17} /></a>
          </div>
        )}
      </div>
      {active && (
        <div className="lightbox" role="dialog" aria-modal="true" aria-label={active.title} onClick={() => setActive(null)}>
          <button onClick={() => setActive(null)} aria-label="Close image"><X /></button>
          <img src={active.src} alt={active.title} referrerPolicy="no-referrer" onError={active.fallback ? e => { e.currentTarget.onerror = null; e.currentTarget.src = active.fallback; } : undefined} onClick={e => e.stopPropagation()} />
          <div><small>{active.source ? `${active.category} · ${active.source}` : active.category}</small><strong>{active.title}</strong></div>
        </div>
      )}
    </section>
  );
}

function GalleryPageHero({ onBook }) {
  return (
    <main className="gallery-page-hero" id="top">
      <div className="gallery-page-hero__image" aria-hidden="true" />
      <div className="gallery-page-hero__shade" />
      <div className="shell gallery-page-hero__content">
        <div className="eyebrow hero__eyebrow"><span /> The Nyota portfolio</div>
        <h1>Our<br /><em>gallery.</em></h1>
        <p>Real inspiration for defining moments—tailoring, ceremony and the exacting work that connects the two.</p>
        <div className="gallery-page-hero__actions">
          <a className="button button--gold" href="#portfolio">Explore the collection <ArrowDown size={17} /></a>
          <button className="button button--ghost" onClick={onBook}>Book your fitting</button>
        </div>
      </div>
      <div className="gallery-page-hero__count"><b>{String(gallery.length).padStart(2, '0')}</b><span>Selected<br />stories</span></div>
    </main>
  );
}

function GalleryCta({ onBook }) {
  return (
    <section className="gallery-cta">
      <div className="gallery-cta__image" aria-hidden="true" />
      <div className="gallery-cta__shade" />
      <div className="shell gallery-cta__content reveal">
        <div className="eyebrow eyebrow--light"><span /> Your turn</div>
        <h2>Inspired?<br /><em>Make it yours.</em></h2>
        <p>Bring us a reference or begin with a blank page. Either way, the finished piece will be unmistakably yours.</p>
        <button className="button button--gold" onClick={onBook}>Begin a consultation <ArrowUpRight size={17} /></button>
      </div>
    </section>
  );
}

function Testimonials() {
  const [index, setIndex] = useState(0);
  const item = testimonials[index];
  const advance = direction => setIndex((index + direction + testimonials.length) % testimonials.length);
  return (
    <section className="testimonials section">
      <div className="shell testimonials__shell reveal">
        <div className="testimonial-mark"><Quote /></div>
        <div className="testimonial-content">
          <div className="testimonial-stars" aria-label="Five stars">{[0,1,2,3,4].map(i => <Star key={i} fill="currentColor" />)}</div>
          <blockquote>“{item.quote}”</blockquote>
          <div className="testimonial-author">
            <div className="testimonial-avatar">{item.name[0]}</div>
            <span><b>{item.name}</b><small>{item.role}</small></span>
          </div>
        </div>
        <div className="testimonial-controls">
          <button onClick={() => advance(-1)} aria-label="Previous testimonial"><ArrowLeft /></button>
          <span>{String(index + 1).padStart(2, '0')} <i /> {String(testimonials.length).padStart(2, '0')}</span>
          <button onClick={() => advance(1)} aria-label="Next testimonial"><ArrowRight /></button>
        </div>
      </div>
    </section>
  );
}

function BookingForm({ compact = false, onSuccess }) {
  const [submitted, setSubmitted] = useState(false);
  const [type, setType] = useState('Bespoke suit');
  const submit = e => {
    e.preventDefault();
    const data = new FormData(e.currentTarget);
    const message = [
      'Hello Nyota Swerve, I would like to request a consultation.',
      '',
      `Name: ${data.get('name')}`,
      `Phone: ${data.get('phone')}`,
      `Outfit: ${data.get('outfit')}`,
      `Preferred date: ${data.get('date')}`,
      data.get('notes') ? `Notes: ${data.get('notes')}` : '',
    ].filter(Boolean).join('\n');
    window.open(`https://wa.me/254795216012?text=${encodeURIComponent(message)}`, '_blank', 'noopener,noreferrer');
    setSubmitted(true);
    if (onSuccess) onSuccess();
  };

  if (submitted) {
    return (
      <div className="form-success">
        <div><Check /></div>
        <h3>Your request is ready.</h3>
        <p>We opened WhatsApp with your appointment details. Tap send there and our atelier will confirm your consultation.</p>
        <button className="underlink" onClick={() => setSubmitted(false)}>Make another request <ArrowRight size={15} /></button>
      </div>
    );
  }

  return (
    <form className={`booking-form ${compact ? 'booking-form--compact' : ''}`} onSubmit={submit}>
      <label><span>Your name</span><input name="name" type="text" placeholder="e.g. James Mwangi" required /></label>
      <label><span>Phone / WhatsApp</span><input name="phone" type="tel" placeholder="+254 7•• ••• •••" required /></label>
      <label className="select-wrap"><span>What are we making?</span>
        <select value={type} onChange={e => setType(e.target.value)} name="outfit">
          <option>Bespoke suit</option><option>Wedding suit</option><option>Groomsmen package</option><option>Tuxedo</option><option>Corporate wear</option><option>Shirt / blazer / trousers</option><option>Alteration or repair</option><option>Other</option>
        </select><ChevronDown />
      </label>
      <label><span>Preferred measurement date</span><input name="date" type="date" min={new Date().toISOString().split('T')[0]} required /></label>
      {!compact && <label className="booking-form__full"><span>Anything we should know?</span><textarea name="notes" placeholder="Tell us about the occasion, date, colour ideas or number of people…" rows="3" /></label>}
      <div className="booking-form__footer booking-form__full">
        <p>By submitting, you agree to be contacted about your request.</p>
        <button className="button button--gold" type="submit">Request appointment <ArrowUpRight size={17} /></button>
      </div>
    </form>
  );
}

function Booking() {
  return (
    <section className="booking section" id="booking">
      <div className="booking__image"><img src={mapsImages[8]} alt="Nyota Swerve tailor at the sewing machine" loading="lazy" referrerPolicy="no-referrer" /><span>Made for one.<br /><em>Made to last.</em></span></div>
      <div className="booking__content reveal">
        <div className="eyebrow eyebrow--light"><span /> Visit the atelier</div>
        <h2>Let’s create<br /><em>your next suit.</em></h2>
        <p>Tell us what you have in mind. We will contact you to confirm timing, consultation details and the next step.</p>
        <BookingForm />
      </div>
    </section>
  );
}

function Journal() {
  return (
    <section className="journal section" id="journal">
      <div className="shell">
        <div className="section-head reveal">
          <div><div className="eyebrow"><span /> The style journal</div><p>05 / 06</p></div>
          <h2>Dress with<br /><em>intention.</em></h2>
          <p>Notes on fit, cloth, occasion and the details that make personal style feel effortless.</p>
        </div>
        <div className="journal-grid">
          {journal.map((article, index) => (
            <article className="journal-card journal-card--text reveal" key={article.title}>
              <div className="journal-card__number">{String(index + 1).padStart(2, '0')}</div>
              <div className="journal-card__meta"><span>{article.category}</span><i />{article.date}</div>
              <h3><a href="#journal">{article.title}</a></h3>
              <p>{article.copy}</p>
              <a className="underlink" href="#journal">Read the note <ArrowRight size={15} /></a>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

function Contact() {
  return (
    <section className="contact" id="contact">
      <div className="contact__info reveal">
        <div className="eyebrow eyebrow--light"><span /> Find us</div>
        <h2>The door is<br /><em>always open.</em></h2>
        <p>Visit our Ruiru atelier for a conversation, a fitting, or simply to explore the cloth.</p>
        <div className="contact-list">
          <a href={whatsappHref} target="_blank" rel="noreferrer"><MessageCircle /><span><small>WhatsApp</small>{phoneDisplay}</span><ArrowUpRight /></a>
          <a href="tel:+254795216012"><Phone /><span><small>Call the atelier</small>{phoneDisplay}</span><ArrowUpRight /></a>
          <a href="mailto:hello@nyotaswerve.co.ke"><Mail /><span><small>Email</small>hello@nyotaswerve.co.ke</span><ArrowUpRight /></a>
          <a href={mapsHref} target="_blank" rel="noreferrer"><MapPin /><span><small>Visit</small>VX8F+FP, Ruiru, Kenya</span><ArrowUpRight /></a>
        </div>
        <div className="opening-hours"><span>Private fittings</span><b>Available by appointment</b></div>
      </div>
      <div className="contact__map">
        <iframe title="Nyota Swerve location in Ruiru" src="https://www.google.com/maps?q=-1.1338746%2C36.9743651&z=17&output=embed" loading="lazy" referrerPolicy="no-referrer-when-downgrade" />
        <div className="map-card"><Brand compact /><p>VX8F+FP, Ruiru, Kenya</p><a href={mapsHref} target="_blank" rel="noreferrer">Get directions <ArrowUpRight /></a></div>
      </div>
    </section>
  );
}

function Footer({ onBook, innerPage = false }) {
  const home = anchor => innerPage ? `/${anchor}` : anchor;
  return (
    <footer>
      <div className="shell footer__top">
        <div className="footer__intro"><Brand homeHref={innerPage ? '/' : '#top'} /><p>Kenyan bespoke tailoring for a life lived with intention.</p><button onClick={onBook}>Book a consultation <ArrowUpRight /></button></div>
        <div className="footer__links"><h4>Explore</h4><a href={home('#story')}>Our story</a><a href={home('#services')}>Services</a><a href={home('#weddings')}>Wedding atelier</a><a href="/gallery">Gallery</a><a href={home('#journal')}>Style journal</a></div>
        <div className="footer__links"><h4>Services</h4><a href={home('#services')}>Bespoke suits</a><a href={home('#weddings')}>Groom packages</a><a href={home('#services')}>Corporate wear</a><a href={home('#services')}>Alterations</a><a href={home('#services')}>Accessories</a></div>
        <div className="footer__social"><h4>Follow the work</h4><a href="https://www.instagram.com/nyota.swerve.closet/" target="_blank" rel="noreferrer"><Instagram />Instagram<ArrowUpRight /></a><a href="https://www.facebook.com/people/Nyotaswervecloset/100083360170098/" target="_blank" rel="noreferrer"><Facebook />Facebook<ArrowUpRight /></a><a href="https://www.tiktok.com/search?q=nyota%20swerve%20closet" target="_blank" rel="noreferrer"><Play />TikTok<ArrowUpRight /></a></div>
      </div>
      <div className="shell footer__bottom"><span>© {new Date().getFullYear()} Nyota Swerve Closet.</span><span>Made in Kenya <Star size={11} fill="currentColor" /></span><div><a href="#top">Privacy</a><a href="#top">Terms</a></div></div>
    </footer>
  );
}

function BookingModal({ open, onClose }) {
  const closeButton = useRef(null);
  useEffect(() => {
    if (open) {
      document.body.classList.add('modal-open');
      setTimeout(() => closeButton.current?.focus(), 50);
    }
    return () => document.body.classList.remove('modal-open');
  }, [open]);
  useEffect(() => {
    const onKey = e => e.key === 'Escape' && onClose();
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [onClose]);
  if (!open) return null;
  return (
    <div className="modal" role="dialog" aria-modal="true" aria-labelledby="booking-title" onMouseDown={e => e.target === e.currentTarget && onClose()}>
      <div className="modal__panel">
        <button className="modal__close" onClick={onClose} ref={closeButton} aria-label="Close booking form"><X /></button>
        <div className="eyebrow"><span /> Private consultation</div>
        <h2 id="booking-title">Begin your<br /><em>Nyota story.</em></h2>
        <p>Share a few details and our atelier will contact you to confirm your appointment.</p>
        <BookingForm compact />
        <div className="modal__direct"><span>Prefer WhatsApp?</span><a href={whatsappHref} target="_blank" rel="noreferrer"><MessageCircle /> Chat with us now</a></div>
      </div>
    </div>
  );
}

function WhatsAppButton() {
  return <a className="whatsapp-float" href={whatsappHref} target="_blank" rel="noreferrer" aria-label="Chat with Nyota Swerve on WhatsApp"><MessageCircle /><span>WhatsApp us</span></a>;
}

function RevealObserver() {
  useEffect(() => {
    const nodes = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window)) {
      nodes.forEach(node => node.classList.add('is-visible'));
      return;
    }
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    nodes.forEach(node => observer.observe(node));
    return () => observer.disconnect();
  }, []);
  return null;
}

function App() {
  const [bookingOpen, setBookingOpen] = useState(false);
  const isGalleryPage = window.location.pathname.replace(/\/+$/, '') === '/gallery';
  const openBooking = () => setBookingOpen(true);

  useEffect(() => {
    window.scrollTo(0, 0);
    document.title = isGalleryPage
      ? 'Gallery | Nyota Swerve Bespoke Tailoring'
      : 'Nyota Swerve | Bespoke Tailoring, Kenya';
  }, [isGalleryPage]);

  if (isGalleryPage) {
    return (
      <>
        <RevealObserver />
        <Header onBook={openBooking} innerPage />
        <GalleryPageHero onBook={openBooking} />
        <Gallery full />
        <GalleryCta onBook={openBooking} />
        <Footer onBook={openBooking} innerPage />
        <BookingModal open={bookingOpen} onClose={() => setBookingOpen(false)} />
        <WhatsAppButton />
      </>
    );
  }

  return (
    <>
      <RevealObserver />
      <Header onBook={openBooking} />
      <Hero onBook={openBooking} />
      <Story />
      <Services />
      <Wedding onBook={openBooking} />
      <Process />
      <Gallery />
      <Testimonials />
      <Booking />
      <Journal />
      <Contact />
      <Footer onBook={openBooking} />
      <BookingModal open={bookingOpen} onClose={() => setBookingOpen(false)} />
      <WhatsAppButton />
    </>
  );
}

createRoot(document.getElementById('root')).render(<App />);
