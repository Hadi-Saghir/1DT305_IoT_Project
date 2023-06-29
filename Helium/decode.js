function Decoder(bytes, port, uplink_info) {
  const decoded = {};

  try {
    const payload = String.fromCharCode.apply(null, bytes);
    const parsedPayload = JSON.parse(payload);
    const { topic, temperature, humidity } = parsedPayload;

    decoded.topic = topic;
    decoded.temperature = temperature;
    decoded.humidity = humidity;
  } catch (error) {
    console.error("Error decoding payload:", error);
  }

  return decoded;
}