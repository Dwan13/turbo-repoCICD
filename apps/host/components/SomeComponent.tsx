const SomeComponent = () => {
    const site = process.env.SITE;
    return (
      <div style={site === 'sitioA' ? { color: 'red' } : { color: 'blue' }}>
        {site === 'sitioA' ? 'Sitio A' : 'Sitio B'}
      </div>
    );
  };
  
  export default SomeComponent;